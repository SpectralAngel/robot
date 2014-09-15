import webiopi
from rrb2 import *
GPIO = webiopi.GPIO
webiopi.setDebug() 

robot = RRB2()


def setup():
    webiopi.debug("Setup")
#   GPIO.setFunction(4, GPIO.OUT)
#   GPIO.setFunction(25, GPIO.OUT)
    flash_lights()
    flash_lights()

def destroy():
    webiopi.debug("Destroy")
    flash_lights()
    flash_lights()
    #flash_lights() flash_lights()

@webiopi.macro
def forward():
    robot.reverse()

@webiopi.macro
def reverse():
    robot.forward()

@webiopi.macro
def stop():
    robot.stop()

@webiopi.macro
def left():
    # turning in small increments, helps with slightly delayed response 
    # on a mobile
    robot.right(8, 1)

@webiopi.macro
def right():
    robot.left(8, 1)

@webiopi.macro
def lights_on():
    robot.set_led1(1)
    robot.set_led2(1)

@webiopi.macro
def lights_off():
    robot.set_led1(0)
    robot.set_led2(0)

@webiopi.macro
def off():
    robot.turn_off()

@webiopi.macro
def on():
    robot.turn_on() 

def flash_lights():
    lights_on()
    webiopi.sleep(0.25)
    lights_off()
    webiopi.sleep(0.25)
