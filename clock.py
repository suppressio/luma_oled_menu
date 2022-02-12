from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1322
from time import sleep
from PIL import ImageFont
import sys, os
import time, datetime

serial = spi(device=0, port=0)
device = ssd1322(serial)

script_dir = os.path.dirname(__file__)
font_dir = os.path.join(script_dir, 'resources/fonts')

small_digit_font = ImageFont.truetype(font_dir + "/digital-7-m.ttf", 18)
medium_digit_font = ImageFont.truetype(font_dir + "/digital-7-mi.ttf", 32)
big_digit_font = ImageFont.truetype(font_dir + "/digital-7-mi.ttf", 46)

lastFrameTime = 0

FPS = 5

def logic(dt):
    # Where speed might be a vector. E.g speed.x = 1 means
    # you will move by 1 unit per second on x's direction.
    #plane.position += speed * dt;

    with canvas(device) as draw:

        draw.text((60, 4), datetime.datetime.now().strftime("%H:%M"), fill="white", font=big_digit_font) 
        draw.text((170, 14), datetime.datetime.now().strftime(":%S"), fill="white", font=medium_digit_font)
        draw.text((90, 45), datetime.datetime.now().strftime("%d-%m-%Y"), fill="white", font=small_digit_font)
        #draw.text((200, 45), datetime.datetime.now().strftime("%p"), fill="white", font=small_digit_font)


        sleepTime = 1./FPS - (currentTime - lastFrameTime)
        if sleepTime > 0:
            time.sleep(sleepTime)

        #time.sleep(1)

while True:
    # dt is the time delta in seconds (float).
    currentTime = time.time()
    dt = currentTime - lastFrameTime
    lastFrameTime = currentTime

    logic(dt)
