import pyautogui

def AFK_mode_1():
    try:
        while True:
            pyautogui.press('1')  # Нажимаем пробел  # Выводим сообщение в консоль
    except KeyboardInterrupt:
        print("Программа остановлена.")

if __name__ == "__main__":
    print("Программа запущена. Нажмите Ctrl+C для выхода.")
    AFK_mode_1()