#pyinstaller -F --icon=app.ico main.py
import keyboard
import pyautogui

welcome_string = 'PlayMine Plugin v1.0\n' \
    '-------------------------------\n' \
    'Alt + 1 : Домой\n' \
    'Alt + 2 : Полет\n' \
    'Alt + 3 : Востановление голода\n' \
    '-------------------------------\n' \
    'Alt + 4 : Магазин\n' \
    'Alt + 5 : Виртуальный верстак\n' \
    '-------------------------------\n' \
    'Alt + 6 : Перенос на Лаки-блоки\n' \
    'Alt + 7 : Перенос на PVP\n' \
    '-------------------------------\n' \
    'Alt + 8 : Спавн\n' \
    'Alt + 9 : Меню\n' \
    '-------------------------------\n' \
    'Alt + R : Перенос в рандомное место \n' \
    '-------------------------------\n' \
    'Ctrl + Q : Exit\n' \
    '-------------------------------\n' \
    'Dev: minesrim'

print(welcome_string)

def send(cmd):
    pyautogui.typewrite('/')
    pyautogui.typewrite(cmd)
    pyautogui.press('enter')

keyboard.add_hotkey('Alt + 1',lambda: send("home"))
keyboard.add_hotkey('Alt + 2',lambda: send("fly"))
keyboard.add_hotkey('Alt + 3',lambda: send("feed"))
keyboard.add_hotkey('Alt + 4',lambda: send("shop"))
keyboard.add_hotkey('Alt + 5',lambda: send("workbench"))
keyboard.add_hotkey('Alt + 6',lambda: send("warp lucky"))
keyboard.add_hotkey('Alt + 7',lambda: send("warp pvp"))
keyboard.add_hotkey('Alt + 8',lambda: send("spawn"))
keyboard.add_hotkey('Alt + 9',lambda: send("menu"))
keyboard.add_hotkey('Alt + R',lambda: send("tpr"))

keyboard.wait('Ctrl + Q')



