#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, UltrasonicSensor
import Movement4 as m
import time

# s
speaker = Sound
mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
cs = ColorSensor()
ts = TouchSensor()
us = UltrasonicSensor()
us.mode = 'US-DIST-CM'
drive = MoveTank(OUTPUT_B, OUTPUT_C)


class GoalAgent1:

    def __init__(self):
        self.percept_sequence = ['White']  # Using list of squares past as apposed to flip variables0. Action methods check last item in the list.ssss
        self.current_black_square = 0
        self.current_travel_direction = 'Horizontal'
        self.distance_until_goal = []
        self.goal_found = False

    def model_based_reflex_agent(self, light_percept):
        """Decides current action. Sends signal to horizontal or vertical action methods depending on direction of travel.s"""
        if self.current_travel_direction == 'Horizontal':
            self.horizontal_action(light_percept)
        elif self.current_travel_direction == 'Vertical':
            self.vertical_action(light_percept)
        else:
            print("t")
            #print(f"Current travel direction error: {self.current_travel_direction} is not an approved value.")

    def horizontal_action(self, light_percept):
        """Initiates horizontal actions once certain conditions are met. Updates percept_sequence, and current_black_square depending on action taken."""
        # Using percept_sequence, and qualified light_percept for immediate human-readable clarity.
        if self.percept_sequence[-1] == 'White' and light_percept == 'Black':
            self.current_black_square += 1
            drive.off()
            speaker.speak(str(self.current_black_square))
            self.percept_sequence.append('Black')

        if self.percept_sequence[-1] == 'Black' and light_percept == 'White':
            self.percept_sequence.append('White')

        if self.current_black_square == 11:
            m.rotate_90_degrees()

    def vertical_action(self, light_percept):
        """Initiates vertical actions once certain conditions are met. Updates percept_sequence, and current_black_square depending on action taken."""
        if self.percept_sequence[-1] == 'White' and light_percept == 'Black':
            self.current_black_square += 15
            drive.off()
            speaker.speak(str(self.current_black_square))
            self.percept_sequence.append('Black')

        if self.percept_sequence[-1] == 'Black' and light_percept == 'Gray' or 'White':
            self.percept_sequence.append('White')

        if self.current_black_square == 56:
            self.find_bottle_with_list()

    def find_bottle_with_list(self):
        """Recursive method that searches for the goal bottle with ultrasonic sensor."""
        # Method needs some more work - analyze best line, then go down line. Figure out bottle square, store location, then set goal_found to True.
        check = 0
        self.distance_until_goal.append(us.distance_centimeters)
        m.left90()
        if check < 2 and self.percept_sequence[-1] == 'Black':
            check += 1
        else:
            drive.off()
            self.find_bottle_with_list()
