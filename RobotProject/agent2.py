#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from framework2 import GoalAgent
import time

ga = GoalAgent()

ga.calibrate_forward()
ga.calibrate_forward()
ga.calibrate_forward()

# rotation calls. Each rotation call should move through white to black, and then through black to the next white. But there is currently trouble at the end to resolve.s
print("rotation 1")
ga.calibrate_rotation()
print("rotation 2")
ga.calibrate_rotation()
print("rotation 3")
ga.calibrate_rotation()
print("rotation 4")
ga.calibrate_rotation()



##while not ga.goal_found:
   ## ga.action(ga.rule())

time.sleep(2)

