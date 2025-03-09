import pyautogui
import time as tm

def AFK_mode():
    try:
        while True:
            pyautogui.press(' ') # Нажимаем пробел  # Выводим сообщение в консоль
            tm.sleep(60)
    except KeyboardInterrupt:
        print("Программа остановлена.")

if __name__ == "__main__":
    print("Программа запущена. Нажмите Ctrl+C для выхода.")
    AFK_mode()
