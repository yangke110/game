import pyautogui as pg
import time

map_name = 'VIP地图'
init_x = 158
init_y = 90
max_x = 10
max_y = 10

click_x = 1
click_y = 1
return_x = 1
return_y = 1


def idle_resume(map_n, cord_x, cord_y, monsters):
    is_out = False
    x_in = True
    # if map_n != map_name:
    #     print("当前所在地图不对!")
    #     return
    if init_x + max_x >= int(cord_x) >= init_x - max_x:
        print("当前仍在挂机x范围内")
    else:
        x_in = False
        print("当前x坐标已超出")
        is_out = True

    if init_y + max_y >= int(cord_y) >= init_y - max_y:
        print("当前仍在挂机y范围内")
        return
    else:
        y_in = False
        print("当前y坐标已超出")
        is_out = True

    if is_out:
        do_return_to()


def do_return_to():
    print("尝试退回至挂机点###############")
    time.sleep(3)
    print("关闭挂机超出对话框")
    pg.moveTo(1275, 927)
    time.sleep(1)
    pg.click(1275, 927)
    time.sleep(1)
    print("尝试打开地图")
    pg.moveTo(2185, 170)
    time.sleep(1)
    pg.click(2185, 170)
    time.sleep(1)
    print("尝试点击挂机点")
    pg.moveTo(899, 532)
    time.sleep(1)
    pg.click(899, 532)
    time.sleep(1)
    print("尝试开始移动")
    pg.moveTo(2049, 1198)
    time.sleep(1)
    pg.click(2049, 1198)
    print("尝试关闭地图")
    pg.moveTo(2112, 230)
    time.sleep(1)
    pg.click(2112, 230)
    time.sleep(10)
    do_auto_idle()


def do_auto_idle():
    pg.press("R")
    time.sleep(1)
    pg.press("3")
