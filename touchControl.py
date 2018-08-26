import subprocess
import threading
from sys import argv
import time


def listen_for_keypress(e, keyboard_id):
    time.sleep(.5)
    p = subprocess.Popen(['xinput', 'test', keyboard_id], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        out = p.stdout.readline()
        e.set()

    
def set_touchpad_state(e, wait_time):
    disabled = False
    while True:
        e.wait(wait_time)

        if e.isSet() and disabled == False :
            # if a new key has been pressed
            print("disabling tap to click")
            # disable tap to click
            subprocess.call(['gsettings', 'set', 'org.gnome.desktop.peripherals.touchpad', 'tap-to-click', 'false'])
            disabled = True

        if not e.isSet() and disabled == True:
            print("enabling tap to click")
            # enable tap to click
            subprocess.call(['gsettings', 'set', 'org.gnome.desktop.peripherals.touchpad', 'tap-to-click', 'true'])
            disabled = False
        e.clear()


if __name__ == '__main__':
    # This is the keyboard ID. It may be different for you.
    # You can find your keyboard ID by typing "xinput list" into your terminal
    # The number you want should be th ID corresponding to "AT Translated Set 2 keyboard", at least it is for me. 
    try:
        keyboard_id = argv[1]
    except IndexError:
        keyboard_id = "16"

    # Number of seconds to wait before enabling tap to click after key is pressed
    # The smaller the number, the sooner tap to click will be enabled after typing
    try:
        wait_time = float(argv[2])
    except IndexError:
        wait_time = 1.5

    e = threading.Event()
    t = threading.Thread(target=listen_for_keypress, args=(e, keyboard_id))
    t.start()

    set_touchpad_state(e, wait_time)
