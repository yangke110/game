import time

import keyboard
from logic import logic_main

if __name__ == '__main__':
    print('Qn Auto Script ,Create By  wadJohnny Yang!\n')
    print('Press F10 to Start...Press F12 to End...')
    while True:
        if keyboard.is_pressed('F10'):
            print('Started')
            logic_main.logic()
 