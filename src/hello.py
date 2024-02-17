import spidev as SPI
import logging
# import sys 
#sys.path.insert(1, '/libs')

from libs import ST7789
import time

from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.DEBUG)
# 240x240 display with hardware SPI:
disp = ST7789.ST7789()

# Initialize library.
disp.Init()

# Clear display.
disp.clear()

#Set the backlight to 100
disp.bl_DutyCycle(50)

# Create blank image for drawing.
#image1 = Image.new("RGB", (disp.width, disp.height), "WHITE")
#draw = ImageDraw.Draw(image1)
#font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)

logging.info("show image")
image = Image.open('monerosigner/assets/guide.png')	
# image = Image.new('RGB', (240, 240), (125, 125, 125))

draw = ImageDraw.Draw(image)
print(image.size)
# draw.line([(20, 10),(70, 60)], fill = "RED",width = 1)
# Draw a black filled box to clear the image.
# draw.rectangle((0,0,disp.width, disp.height), outline=0, fill=0)


class gridView:

    def __init__(self, _draw):
        self.BOXCONSTANTS = BOXCONSTANTS()
        self.draw = _draw
    def drawBoxAtPosition(self, _position):
        gridLocation = self.BOXCONSTANTS.gridLocation[_position]
        self.draw.rectangle((gridLocation,(BOXCONSTANTS.width + gridLocation[0] , BOXCONSTANTS.height + gridLocation[1])), fill = None, outline = "RED")

class BOXCONSTANTS:
    # width = 48
    # height = 131
    width = 108 
    height = 84
    gridLocation = {}
    gridLocation[0] = (8,48)
    gridLocation[1] = (124,48)
    gridLocation[2] = (8,136)
    gridLocation[3] = (124,136)




#highlight first box 
# draw.rectangle((0,0,100,100), fill = "BLUE")
# draw.rectangle(((8,48),(116, 131)), outline="RED", fill="RED", width=0)
# draw.rectangle((124,48,124 + BOXCONSTANTS.width,BOXCONSTANTS.height + 48), fill = "GREEN")
gridView = gridView(draw)
gridView.drawBoxAtPosition(0)
gridView.drawBoxAtPosition(1)
gridView.drawBoxAtPosition(2)
gridView.drawBoxAtPosition(3)






# disp.ShowImage(image)

#im_r=image.rotate(270)
# im_r=image.rotate(0)
disp.ShowImage(image)

time.sleep(3)
input("enter to quit")
disp.clear()
# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image1 = Image.new("RGB", (disp.width, disp.height), "WHITE")

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image1)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,disp.width, disp.height), outline=0, fill=0)
disp.ShowImage(image1)
