# from libs import ST7789
import threading
import time
from monerosigner.boot import ViewController

from PIL import Image,ImageDraw,ImageFont

#this class helps us keep track of the current state 
class AppControl:
    def __init__(self):
        self.alive = False

    def initiate(self):
        self.alive = True
    def kill(self):
        self.alive = False
    def isAlive(self):
        return self.alive
    

AppControl = AppControl()
ViewController = ViewController()
ViewController.splashScreen()
ViewController.guide()


AppControl.initiate()


# image1 = Image.new("RGB", (disp.width, disp.height), "WHITE")
# draw = ImageDraw.Draw(image1)

while True:
    if ViewController.disp.digital_read(ViewController.disp.GPIO_KEY1_PIN) == 1: # button is released
        #  draw.ellipse((70,0,90,20), outline=255, fill=0xff00) #A button
         AppControl.kill()
    if ViewController.disp.digital_read(ViewController.disp.GPIO_KEY_LEFT_PIN) == 0:
             # button is released
            ViewController.draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0xff00)  #left           
    else: # button is pressed:
        ViewController.draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  #left filled
        print ("left") 
    if AppControl.isAlive() == False:
            print("Killing tasks")
            break
    ViewController.refreshScreen()