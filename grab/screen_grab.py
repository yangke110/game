import configparser

from PIL import ImageGrab

import easyocr
reader = easyocr.Reader(['ch_sim'], gpu=True)


def get_map_name(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    map_name:str = config['basic']['map_name']
    map_name_list = map_name.split(',')
    img = (int(map_name_list[0]), int(map_name_list[1]), int(map_name_list[2]), int(map_name_list[3]))  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../map_name.png")

    result = reader.readtext('../map_name.png')
    text = ""
    for r in result:
        text += r[1]
    return text


def get_map_x(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    map_x: str = config['basic']['cord_x']
    mmap_x_list = map_x.split(',')
    img = (int(mmap_x_list[0]), int(mmap_x_list[1]), int(mmap_x_list[2]), int(mmap_x_list[3]))  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../map_x.png")

    result = reader.readtext('../map_x.png')
    text = ""
    for r in result:
        text += r[1]
    return text


def get_map_y(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    map_y: str = config['basic']['cord_y']
    map_y_list = map_y.split(',')
    img = (int(map_y_list[0]), int(map_y_list[1]), int(map_y_list[2]), int(map_y_list[3]))  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../map_y.png")

    result = reader.readtext('../map_y.png')
    text = ""
    for r in result:
        text += r[1]
    return text


def get_monsters(config_path):
    config = configparser.ConfigParser()
    config.read(config_path)
    monsters: str = config['basic']['monsters']
    monsters_list = monsters.split(',')
    img = (int(monsters_list[0]), int(monsters_list[1]), int(monsters_list[2]), int(monsters_list[3]))  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../monsters.png")

    result = reader.readtext('../monsters.png')
    text = ""
    for r in result:
        text += r[1]
    return text