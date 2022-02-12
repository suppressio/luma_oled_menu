from luma.core.interface.serial import spi
from luma.core.render import canvas
from luma.oled.device import ssd1322
from time import sleep
from PIL import ImageFont
from RPi import GPIO
import sys, os
import time

import menu
import xmlConfigs

serial = spi(device=0, port=0)
device = ssd1322(serial)

script_dir = os.path.dirname(__file__)
font_dir = os.path.join(script_dir, 'resources/fonts')

icons_font = ImageFont.truetype(font_dir + "/fa-font.otf", 18)
small_font = ImageFont.truetype(font_dir + "/small_pixel-7.ttf", 15)

lastFrameTime = 0

FPS = 60

gpio_clk = 17
gpio_dt = 18
gpio_sw = 27

def init_menu():
    menu_0 = [];
    menu_0_style = xmlConfigs.getLvlStyle("0", "")

    for me in xmlConfigs.getMG_elements("0", ""):
        menu_0.append(
            menu.Menu(
                int(xmlConfigs.getId(me)),
                xmlConfigs.getName(me),
                chr(int(xmlConfigs.getIcon(me),base=16)),
                xmlConfigs.getIconStyle(me),
                xmlConfigs.getDescription(me),
                "")) # TODO:  commands
    return menu_0

def logic(dt, i, menu_0):

    with canvas(device) as draw:
        menu.draw_lines(draw)

        for m0 in menu_0:
        #m0 = menu_0[0]
            menu.draw_graph_menu_element(draw,
                    m0.id,
                    (i == m0.id),
                    m0.icon,
                    icons_font) # FIXME me.icon_style

            if (i == m0.id):
                menu.draw_descr_command(draw,
                    m0.description,
                    small_font)


        sleepTime = 1./FPS - (currentTime - lastFrameTime)
        if sleepTime > 0:
            time.sleep(sleepTime)

        #time.sleep(1)


try:

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(gpio_clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gpio_dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(gpio_sw, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    counter = 0
    clkLastState = GPIO.input(gpio_clk)
    menu_0 = init_menu()

    while True:
        currentTime = time.time()
        dt = currentTime - lastFrameTime
        lastFrameTime = currentTime

        logic(dt, counter, menu_0)

        clkState = GPIO.input(gpio_clk)
        dtState = GPIO.input(gpio_dt)
        if clkState != clkLastState:
            if dtState != clkState:
                counter = (counter+1) % 17
                #print("DX")
            else:
                counter = (counter-1) % 17
                #print("SX")
            #print(counter)
        clkLastState = clkState

        if GPIO.input(gpio_sw) == GPIO.LOW:
            button += 1
        if GPIO.input(gpio_sw) == GPIO.HIGH:
            button = 0
        if button == 1:
            print("Button")

finally:
        GPIO.cleanup()
