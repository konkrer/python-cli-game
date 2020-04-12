from PIL import Image, ImageDraw, ImageFont
import math
#This file i got from:  Raphson
#https://www.youtube.com/watch?v=2fZBLPk-T2Y&list=LL19PJgf0W2Eq6lV-QVnDt2A&index=3&t=917s
#did some minor tweaks...
chars = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\\|()1{}[]?-_+~<>i!lI;:,\"^`'. "[::-1]

charArray = list(chars)
charLength = len(charArray)
interval = charLength/256

scaleFactor = 0.09

oneCharWidth = 10
oneCharHeight = 18


def getChar(inputInt):
    return charArray[math.floor(inputInt*interval)]


text_file = open("Output.txt", "w")

im = Image.open("Mad_Libs_logo.jpg")
#You may have to chage this line to a font on your system too work this is my relative path
fnt = ImageFont.truetype('/System/Library/Fonts/Supplemental/Arial Unicode.ttf', 15)

width, height = im.size
im = im.resize((int(scaleFactor*width), int(scaleFactor * height * (oneCharWidth/oneCharHeight))), Image.NEAREST)
width, height = im.size
pix = im.load()

outputImage = Image.new('RGB', (oneCharWidth * width, oneCharHeight * height), color=(0, 0, 0))
d = ImageDraw.Draw(outputImage)

for i in range(height):
    for j in range(width):
        r, g, b = pix[j, i]
        h = int(r/3 + g/3 + b/3)
        pix[j, i] = (h, h, h)
        text_file.write(getChar(h))
        d.text((j*oneCharWidth, i*oneCharHeight),
               getChar(h), font=fnt, fill=(r, g, b))

    text_file.write('\n')

outputImage.save('output.png')
