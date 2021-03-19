#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank

drive = MoveTank(OUTPUT_B, OUTPUT_C)

drive.off