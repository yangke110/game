import time
import pyautogui as pg
from grab import screen_grab
from logic import fox_logic
from logic.idle import idle_resume

action_type = "fox"  # 脚本类型

map_n = ""
cord_x = 0
cord_y = 0
monsters = ""

load_duration = 0.2


def logic(case: int):
    # focus_on_screen()
    while True:
        load_info()
        print(f"当前人物所在位置 {map_n} {cord_x} : {cord_y}")
        print(f"当前人物附近怪物 {monsters}")
        # do_actions(map_n, cord_x, cord_y, monsters)
        if case == 1:
            # 狐狸洞
            do_actions()
        elif case == 2:
        # 极乐洞
            return
        elif case == 3:
            idle_resume(map_n, cord_x, cord_y, monsters)
        time.sleep(load_duration)


def load_info():
    # 像素2560 x 1440
    # 获取当前地图 左 2040 上 40 右 375 下1350
    global map_n, cord_x, cord_y, monsters
    map_n = screen_grab.get_map_name()
    cord_x = screen_grab.get_map_x()
    cord_y = screen_grab.get_map_y()
    monsters = screen_grab.get_monsters()


def do_actions(map_n, cord_x, cord_y, monsters):
    if action_type == 'fox':
        fox_logic.do_fox_logic(map_n, cord_x, cord_y, monsters)


def focus_on_screen():
    # 点击主屏幕切换焦点
    pg.moveTo(300, 300)
    pg.click
