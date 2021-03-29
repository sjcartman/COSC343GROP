#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, UltrasonicSensor
# import Movements4 as m
from gf4 import GoalAgent
import time

# robot module inistiation
drive = MoveTank(OUTPUT_B, OUTPUT_C)
ga = GoalAgent1()

# move to first black tile - used values 20, 20, 0.85
drive.on_for_rotations(20, 20, 1.7)
ga.right90()

print('start done')
count = 1
while not ga.goal_found:
    print("\nLoop # " + str(count))
    light_input = ga.light_transition_model(10)
    print('light:' + light_input)
    drive.on(SpeedPercent(20), SpeedPercent(20))
    print('drive on')
    ga.model_based_reflex_agent(light_input)
    print('reflex done, current black square = ' + str(ga.current_black_square))
    count = count + 1

# todo: set up correction feedback from timing distance until each black, and correcting if distance becomes over.
# todo: get find_bottle method working with moving forwards and backwards, and returning bottle location when found.
