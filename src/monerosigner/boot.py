import spidev as SPI
import logging

from libs import ST7789
import time

from PIL import Image,ImageDraw,ImageFont

class ViewController:
    def __init__(self):
        self.version = "0.0.1"
        self.disp = ST7789.ST7789()
        # Initialize library.
        self.disp.Init()
        # Clear display.
        self.disp.clear()
        self.image = Image.open('monerosigner/assets/guide.png')	
        self.draw = ImageDraw.Draw(self.image)
    def splashScreen(self):
        logging.info("Init splash screen")
        #Set the backlight to 100
        self.disp.bl_DutyCycle(50)

        # Create blank image for drawing.
        #image1 = Image.new("RGB", (disp.width, disp.height), "WHITE")
        #draw = ImageDraw.Draw(image1)
        #font = ImageFont.truetype('/usr/share/fonts/truetype/freefont/FreeMonoBold.ttf', 16)

        logging.info("show image")
        image = Image.open('logo_black_240.png')	
        #im_r=image.rotate(270)
        im_r=image.rotate(0)
        self.disp.ShowImage(im_r)

        time.sleep(3)
    def guide(self):
        self.disp.clear()

        #Set the backlight to 100
        self.disp.bl_DutyCycle(50)

        logging.info("show image")
        # image = Image.open('monerosigner/assets/guide.png')	
        # im_r=image.rotate(0)
        # self.disp.ShowImage(im_r)
        self.draw.line([(20, 10),(70, 60)], fill = "RED",width = 1)
        self.disp.ShowImage(self.image)

        # time.sleep(3)
    def refreshScreen(self):
        self.disp.ShowImage(self.image)