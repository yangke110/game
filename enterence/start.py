import keyboard
from logic import logic_main

if __name__ == '__main__':
    print('Qn Auto Script ,Create By  Johnny Yang!\n')
    print('Press F10 to Start...Press F12 to End...')
    while True:
        if keyboard.is_pressed('F10'):
            print('Started')
            # logic_main.logic(1)
            print('挂机被拖自动恢复')
            logic_main.logic(3,'../config_hm.ini')

 