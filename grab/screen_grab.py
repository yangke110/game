from PIL import ImageGrab

import easyocr
reader = easyocr.Reader(['ch_sim'], gpu=True)


def get_map_name():
    img = (2040, 40, 2188, 90)  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../map_name.png")

    result = reader.readtext('../map_name.png')
    text = ""
    for r in result:
        text += r[1]
    return text


def get_map_x():
    img = (2220, 40, 2288, 90)  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../map_x.png")

    result = reader.readtext('../map_x.png')
    text = ""
    for r in result:
        text += r[1]
    return text


def get_map_y():
    img = (2320, 40, 2390, 90)  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../map_y.png")

    result = reader.readtext('../map_y.png')
    text = ""
    for r in result:
        text += r[1]
    return text


def get_monsters():
    img = (1086, 450, 1400, 870)  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../monsters.png")

    result = reader.readtext('../monsters.png')
    text = ""
    for r in result:
        text += r[1]
    return text