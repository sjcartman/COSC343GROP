#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, TouchSensor
from Goal_framework import GoalAgent
import time



speaker = Sound()
mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
cs = ColorSensor()
ts = TouchSensor()
drive = MoveTank(OUTPUT_B, OUTPUT_C)
flip = True
turn_left_on_grey = False
count = 0
ga = GoalAgent()
vert = False
#ga.move('spin', 10, 10, 1)
ga.var_forward(0.8)
ga.right90()
#s
while True:
    if ts.is_pressed:
        drive.off()
        break

    value = 0
    drive.on(SpeedPercent(20), SpeedPercent(20))
    if count == 11 and not vert:
        print("s " + str(cs.reflected_light_intensity) + " " + str(count))
        drive.off()
        time.sleep(1)
        ga.right90()
        #count = count + 15
        vert = True
    elif (cs.color == 1 and flip) or (cs.color == 6 and not flip):
        print("e " + str(cs.reflected_light_intensity) + " " + str(count))
        #drive.off()
        #time.sleep(.5)
        if flip:
            count = count + 1
            if vert:
                count = count + 14
            speaker.speak(str(count))
        if count == 56:
            break
        flip = not flip

    #elif cs.reflected_light_intensity > 30 and cs.reflected_light_intensity < 40 and value %10 == 0:
     #   print("y " + str(cs.reflected_light_intensity) + " " + str(count))
      #  drive.off()
       # time.sleep(.5)
        #if turn_left_on_grey :
         #   ga.right9()
        #else :
         #   ga.left9()
        #turn_left_on_grey = not turn_left_on_grey

