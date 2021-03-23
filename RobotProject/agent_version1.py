#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from Goal_framework import GoalAgent
import time


mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
cs = ColorSensor()
drive = MoveTank(OUTPUT_B, OUTPUT_C)
flip = True
turn_left_on_grey = false
count = 0
ga = GoalAgent()

#ga.move('spin', 10, 10, 1)sssssss
ga.var_forward(0.8)
ga.right()
while True:
    drive.on(SpeedPercent(20), SpeedPercent(20))
    if (cs.reflected_light_intensity <= 10 and flip) or (cs.reflected_light_intensity >= 90 and not flip):
        drive.off()
        time.sleep(.5)
        flip = not flip
        if flip:
            count = count +1
    elif(count == 13):
        drive.off()
        time.sleep(1)
        ga.right()
        count = count + 16
    if (cs.reflected_light_intensity > 10 and cs.reflected_light_intensity < 90) :
        drive.off()
        time.sleep(.5)



for i in range(1,12):
    ga.straight_horizontal_one_tile()
    time.sleep(2)




