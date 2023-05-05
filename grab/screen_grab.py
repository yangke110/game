from PIL import ImageGrab

import easyocr
reader = easyocr.Reader(['ch_sim'], gpu=True)


def get_map_name():
    img = (2037, 40, 2181, 87)  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../map_name.png")

    result = reader.readtext('../map_name.png')
    text = ""
    for r in result:
        text += r[1]
    return text


def get_map_x():
    img = (2222, 41, 2302, 83)  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../map_x.png")

    result = reader.readtext('../map_x.png')
    text = ""
    for r in result:
        text += r[1]
    return text


def get_map_y():
    img = (2323, 41, 2388, 85)  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../map_y.png")

    result = reader.readtext('../map_y.png')
    text = ""
    for r in result:
        text += r[1]
    return text


def get_monsters():
    img = (433, 169, 775, 464)  # 距离左上右下的像素
    loc_img = ImageGrab.grab(img)
    loc_img.save("../monsters.png")

    result = reader.readtext('../monsters.png')
    text = ""
    for r in result:
        text += r[1]
    return text