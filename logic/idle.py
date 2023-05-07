import pyautogui as pg
import time
import configparser

map_name = 'VIP地图'
init_x = 158
init_y = 90
max_x = 10
max_y = 10

click_x = 1
click_y = 1
return_x = 1
return_y = 1


def idle_resume(map_n, cord_x, cord_y, monsters, config_path):
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
        do_return_to(config_path)


def do_return_to(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    print("尝试退回至挂机点###############")
    time.sleep(3)
    print("关闭挂机超出对话框")
    close_con = config['idle']['close_con']
    close_con_list = close_con.split(',')
    pg.moveTo(int(close_con_list[0]), int(close_con_list[1]))
    time.sleep(1)
    pg.click(int(close_con_list[0]), int(close_con_list[1]))
    time.sleep(1)
    print("尝试打开地图")
    open_map = config['idle']['open_map']
    open_map_list = open_map.split(',')
    pg.moveTo(int(open_map_list[0]), int(open_map_list[1]))
    time.sleep(1)
    pg.click(int(open_map_list[0]), int(open_map_list[1]))
    time.sleep(1)
    print("尝试点击挂机点")
    idle_loc = config['idle']['idle_loc']
    idle_loc_list = idle_loc.split(',')
    pg.moveTo(int(idle_loc_list[0]), int(idle_loc_list[1]))
    time.sleep(1)
    pg.click(int(idle_loc_list[0]), int(idle_loc_list[1]))
    time.sleep(1)
    print("尝试开始移动")
    start_move = config['idle']['start_move']
    start_move_list = start_move.split(',')
    pg.moveTo(int(start_move_list[0]), int(start_move_list[1]))
    time.sleep(1)
    pg.click(int(start_move_list[0]), int(start_move_list[1]))
    print("尝试关闭地图")
    close_map = config['idle']['close_map']
    close_map_list = close_map.split(',')
    pg.moveTo(int(close_map_list[0]), int(close_map_list[1]))
    time.sleep(1)
    pg.click(int(close_map_list[0]), int(close_map_list[1]))
    time.sleep(10)
    do_auto_idle()


def do_auto_idle():
    pg.press("R")
    time.sleep(1)
    pg.press("3")
