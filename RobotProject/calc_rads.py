#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
import time
import sys, math
from Goal_framework import GoalAgent
ga = GoalAgent()

f = open("rads.txt", "a")

for i in range(0,5):
    t = time.time()
    ga.right90()
    t1 = time.time()-t
    ga.right90()
    t2 = time.time()-t
    ga.right90()
    t3 = time.time()-t
    f.write(str(t1)+"\t"+str(t2)+"\t"+str(t3)+"\t"+"\n")
f.close()
