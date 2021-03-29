#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
import math
# import Movements4 as m
import time

# s
speaker = Sound()
mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
cs = ColorSensor()
us = UltrasonicSensor()
drive = MoveTank(OUTPUT_B, OUTPUT_C)


class GoalAgent:

    def __init__(self):
        self.percept_sequence = [
            'Black']  # Using list of squares past as apposed to flip variable. Action methods check last item in the lists.
        self.current_black_square = 1
        self.current_travel_direction = 'Horizontal'
        self.distance_until_goal = []
        self.goal_found = False

    def model_based_reflex_agent(self, light_percept):
        """Decides current action. Sends signal to horizontal or vertical action methods depending on direction of travel."""
        if self.current_travel_direction == 'Horizontal':
            self.horizontal_action(light_percept)
        elif self.current_travel_direction == 'Vertical':
            self.vertical_action(light_percept)
        else:
            pass

    def horizontal_action(self, light_percept):
        """Initiates horizontal actions once certain conditions are met. Updates percept_sequence, and current_black_square depending on action taken."""
        # Using percept_sequence, and qualified light_percept for immediate human-readable clarity.
        if self.percept_sequence[-1] == 'White' and light_percept == 'Black':
            self.current_black_square = self.current_black_square + 1
            drive.off()
            time.sleep(1)
            speaker.speak(str(self.current_black_square))
            self.percept_sequence.append('Black')
            #print(f"Action #1. Last percept sequence = {self.percept_sequence}, light_percept = {light_percept}")
            self.calibrate()

        elif self.percept_sequence[-1] == 'Black' and light_percept == 'White':
            self.percept_sequence.append('White')
            #print(f"Action #2. percept sequence = {self.percept_sequence}, light_percept = {light_percept}")

        else:
            pass
            # print(f"No action. Last percept sequence = {self.percept_sequence}, light_percept = {light_percept}")

        if self.current_black_square == 11:
            self.rotate_90_degrees()

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
            print('finding bottle with list')
            self.find_bottle_with_list()

    def find_bottle_with_list(self):
        """Recursive method that searches for the goal bottle with ultrasonic sensor."""
        # Method needs some more work - analyze best line, then go down line. Figure out bottle square, store location, then set goal_found to True.
        check = 0
        self.distance_until_goal.append(us.distance_centimeters)
        self.left90()
        if check < 2 and self.percept_sequence[-1] == 'Black':
            check += 1
        else:
            drive.off()
            self.find_bottle_with_list()

    def calibrate(self):
        """Note: this seems to correct the robot in the simulator, but I have no idea why - Taya."""
        # test which side is closer
        drive.off

        # check left lean
        counter = 0
        while cs.reflected_light_intensity < 25:
            drive.on_for_rotations(-13, 13, 0.1)
            counter = counter + 1

        # reset
        drive.on_for_rotations(13, -13, 0.1*counter)

        # check right lean
        counter2 = 0
        while cs.reflected_light_intensity < 25:
            drive.on_for_rotations(13, -13, 0.0)
            counter2 = counter2 + 1

        # reset
        drive.on_for_rotations(-13, 13, 0.1*counter2)

        # A calibration strategy that might work for physical robot
        """  # test which side is closer
        drive.off

        # Working values at -8, 13, 0.01, and the inverses

        # check left lean
        counter = 0
        while cs.reflected_light_intensity < 25:
            drive.on_for_rotations(-8, 13, 0.01)
            counter = counter + 1

        # reset
        self.calibrate_data.append(counter)
        print(self.calibrate_data[-1])
        print(f"Rotating {counter + 10*(math.log(30/counter))}")
        drive.on_for_rotations(8, -13, 0.01*counter + 0.1*(math.log(30/counter)))

        # check right lean
        counter2 = 0
        while cs.reflected_light_intensity < 25:
            drive.on_for_rotations(13, -8, 0.01)
            counter2 = counter2 + 1

        # reset
        self.calibrate_data.append(counter2)
        print(self.calibrate_data[-1])
        print(f"Rotating {counter2 + 10 * (math.log(30 / counter2))}")
        drive.on_for_rotations(-13, 8, 0.01*counter2 + 0.1*(math.log(30/counter2)))

        print(f"Counter 1: {counter}, Counter 2: {counter2}")
        print(f"Average rotation count =  {sum(self.calibrate_data)/len(self.calibrate_data)}")
        print(self.calibrate_data)

        """





    # Movement actions
    def light_transition_model(self, num_of_readings):
        # get average of X number of light intensity readings

        light_level = 0
        for _ in range(num_of_readings):
            light_level = light_level + cs.reflected_light_intensity
        light_level = light_level / num_of_readings
        # light levels, <15, >45, >20
        if light_level < 15:
            return 'Black'
        elif light_level >= 34:
            return 'White'
        elif light_level > 100:
            return 'Gray'

    def rotate_90_degrees(self):
        drive.off()  # stop
        drive.on_for_rotations(20, 20, 0.45)  # var forward
        time.sleep(1)  # waits
        drive.on_for_rotations(13, -13, 0.95 / 2)  # turn 90 degrees to the right - current values 13, -13, 0.95/2
        if self.current_travel_direction == 'Horizontal':
            self.current_travel_direction = 'Vertical'
        else:
            self.current_travel_direction = 'Horizontal'

    def left90(self):
        drive.on_for_rotations(-13, 13, 0.95 / 2)

    def right90(self):
        drive.on_for_rotations(13, -13, 0.95/2)