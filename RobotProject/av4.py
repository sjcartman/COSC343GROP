#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, UltrasonicSensor
# import Movements4 as m
from gf4 import GoalAgent1

# robot module initssiationss
drive = MoveTank(OUTPUT_B, OUTPUT_C)
ga = GoalAgent1()

# move to first black tile - used values 20, 20, 0.85
drive.on_for_rotations(20, 20, 0.85)
ga.right90()


while not ga.goal_found:
    light_input = ga.light_transition_model(10)
    drive.on(SpeedPercent(20), SpeedPercent(20))
    ga.model_based_reflex_agent(light_input)



