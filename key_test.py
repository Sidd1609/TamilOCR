import keyboard
import sys
while True:
    if not keyboard.is_pressed('space'):
        print(0)
    elif keyboard.is_pressed('q'):
        sys.exit()
