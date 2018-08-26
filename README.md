# Disable Touchpad While Typing
Disables touchpad while typing. Tested on Ubuntu 18.04

This is a python3 script that disables your touchpad's "touch to click" while you're typing.

To use, you'll first need to find your keyboard ID. You can find your keyboard ID by typing "xinput list" into your terminal.

The number you want should be the ID corresponding to "AT Translated Set 2 keyboard", at least it is for me.

The script takes 2 arguments. 

arg1: Your keyboard ID

arg2: The number of seconds to wait before enabling the touchpad after typing (default is 1.5)

So, use it like this:

python3 touchControl.py 16 1.5
