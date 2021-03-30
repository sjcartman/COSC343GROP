#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, UltrasonicSensor
from Goal_framework4 import GoalAgent
import time

# s

cs = ColorSensor()
drive = MoveTank(OUTPUT_B, OUTPUT_C)
ga = GoalAgent()


def light_transition_model(num_of_readings, light_level=None):
    # get average of X number of light intensity readingsssssss
    for _ in range(num_of_readings):
        light_level += cs.reflected_light_intensity
    light_level = light_level / num_of_readings

    if light_level < 15:
        return 'Black'
    elif light_level > 45:
        return 'White'
    elif light_level > 20:
        return 'Gray'


def rotate_90_degrees():
    drive.off()  # stop
    drive.on_for_rotations(20, 20, 0.45)  # var forward
    time.sleep(1)  # waits
    drive.on_for_rotations(13, -13, 0.95 / 2)  # turn 90 degrees to the right
    if ga.current_travel_direction == 'Horizontal':
        ga.current_travel_direction = 'Vertical'
    else:
        ga.current_travel_direction = 'Horizontal'


def left90():
    drive.on_for_rotations(-13, 13, 0.95 / 2)


def right90():
    drive.on_for_rotations(13, -13, 0.95 / 2)

# todo: make left90 and right90 automatically update current_travel_direction.