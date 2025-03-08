import pyautogui

def press_space_every_minute():
    try:
        while True:
            pyautogui.press('1')  # Нажимаем пробел  # Выводим сообщение в консоль
    except KeyboardInterrupt:
        print("Программа остановлена.")

if __name__ == "__main__":
    print("Программа запущена. Нажмите Ctrl+C для выхода.")
    press_space_every_minute()