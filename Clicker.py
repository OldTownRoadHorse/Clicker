import pyautogui
from pynput.keyboard import Listener, Key

pstm = 100000
resume_key = Key.f2
pause_key = Key.f3
exit_key = Key.f4


pause = True
running = True

def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Начало]")
    elif key == pause_key:
        pause = True
        print("[Пауза]")
    elif key == exit_key:
        running = False
        print("[Выход]")


def display_controls():
    print("\t F2 = Начать")
    print("\t F3 = Пауза")
    print("\t F4 = Выход")


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
      if not pause:
        try:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = pstm
        except Exception as e:
            print(e)
    lis.stop()


if __name__ == "__main__":
    main()