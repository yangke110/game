import time

from PIL import ImageGrab

import easyocr
import torch

reader = easyocr.Reader(['ch_sim'], gpu=True)
if __name__ == '__main__':

    location = (1520, 35, 1800, 100)
    loc_img = ImageGrab.grab(location)

    loc_img.save('location.png')

    # 分析图片上的文字
    while True:

        result = reader.readtext('location.png')
        text = ""
        for r in result:
            text += r[1]
        print(text)
        time.sleep(0.1)
