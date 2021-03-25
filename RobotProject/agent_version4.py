#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, UltrasonicSensor
from Goal_framework4 import GoalAgent
import Movements4 as m
import time

# robot module initiation
drive = MoveTank(OUTPUT_B, OUTPUT_C)
ga = GoalAgent()

# move to first black tile
drive.on_for_rotations(20, 20, 0.85)
m.right90()

while not ga.goal_found:
    light_input = m.light_transition_model(10)
    drive.on(SpeedPercent(20), SpeedPercent(20))
    ga.model_based_reflex_agent(light_input)

# todo: set up correction feedback from timing distance until each black, and correcting if distance becomes over.
# todo: get find_bottle method working with moving forwards and backwards, and returning bottle location when found.
