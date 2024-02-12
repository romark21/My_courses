import winreg

import pyautogui as pg


# print(pg.position())
#
# pg.leftClick(1148, 90)
# pg.typewrite("google.com")
# pg.typewrite(["enter"])
# pg.hotkey("Winleft")
# pg.typewrite("chrome\n", 0.5)
# pg.typewrite("www.youtube.com\n", 0.2)
# pg.hotkey("winleft", "up")
# pg.hotkey("ctrl", "t")
# import getpass
# USER_NAME = getpass.getuser()
#
#
# def add_to_startup(file_path=""):
#     if file_path == "":
#         file_path = os.path.dirname(os.path.realpath(__file__))
#     bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % (USER_NAME)
#     with open(bat_path + '\\open.bat', 'w') as bat_file:
#         bat_file.write(r'start %s' % (file_path))
# add_to_startup()

def auto_run():
    # Добавить в автозагрузку
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run", 0,
                         winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(key, "Date Time", 0, winreg.REG_SZ,
                      "C:\\Users\\Robert\\OneDrive\\Рабочий стол\\pythonProject1\\Решение разных задач")
    key.Close()


def windows_with_messege():
    pg.alert(text='Привет, Ты точно играть хочешь?', title='Ахтунг ёмоё', button='Да')
    pg.alert(text='Ладно, но с условием. Ты должен ответить на вопрос. Согласен?', title='Без вариантов', button='Да')
    answear = pg.prompt("Сколько будет 2 + 2 ?")
    if answear == "4":
        pg.alert(text='Ты такой умный… Череп не жмет?', title='И ты получаешь теле-медаль', button='Ок')
    else:
        pg.alert(text='Может, лучше почитать?', title='Упссс', button='Ок')


auto_run()
windows_with_messege()
