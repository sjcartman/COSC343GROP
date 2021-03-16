#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
from Goal_framework import GoalAgent


mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
drive = MoveTank(OUTPUT_B, OUTPUT_C)


ga = GoalAgent()

ga.move('spin', 10, 10, 1.5)
<<<<<<< HEAD
#ss
=======

>>>>>>> 353b2604f1d345f1e85cde8d2812ff0d9012b53e


