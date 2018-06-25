# 将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。 类似于图中效果
# -*- coding:'utf-8' -*-

import PIL
from PIL import Image, ImageDraw, ImageFont


imageFile='test.jpg'
im1=Image.open(imageFile)

font=ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', 30)

draw=ImageDraw.Draw(im1)
draw.text((160,20),u"4", (255,0,0),font=font)


draw=ImageDraw.Draw(im1)
im1.save('target_01.png')