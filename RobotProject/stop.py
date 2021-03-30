#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, TouchSensor
from Goal_framework import GoalAgent
import time
drive = MoveTank(OUTPUT_B,OUTPUT_C)
drive.off()
quit()