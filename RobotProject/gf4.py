#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
import math
# import Movements4 as m
import time

# ss
speaker = Sound()
mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
cs = ColorSensor()
us = UltrasonicSensor()
drive = MoveTank(OUTPUT_B, OUTPUT_C)


class GoalAgent1:

    def __init__(self):
        self.percept_sequence = [
            'White']  # Using list of squares past as apposed to flip variable. Action methods check last item in the lists.
        self.current_black_square = 0
        self.current_travel_direction = 'Vertical'
        self.calibrate_data = []
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
            self.correction()

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

    def correction(self):
        # move forward to be more on the tile
        self.var_forward(0.1)
        # start the timer
        start_time = time.time()
        while True:
            # move left(because right wheel is turned on)s
            mRight.on(SpeedPercent(20))
            # if light reflected is not black
            if cs.reflected_light_intensity > 30:
                # record the time
                end_time = time.time()
                # save it into a value
                value = end_time - start_time
                # stop the motors
                drive.off()
                # break out of the surrounding while loop
                break
        # return back to normal position
        mRight.on_for_seconds(SpeedPercent(-20), value)
        # repeat the above for the right(left wheel now turned on)
        start_time = time.time()
        while True:
            mLeft.on(SpeedPercent(20))
            if cs.reflected_light_intensity > 30:
                end_time = time.time()
                value2 = end_time - start_time
                drive.off()
                break
        mLeft.on_for_seconds(SpeedPercent(-20), value2)
        # round the values off to get an estimate(to 1 decimal place? not sure if it works)
        value2 = float("{:.1f}".format(value2))
        value = float("{:.1f}".format(value))
        # if one is higher, turn one way by 25 degrees, else turn other, else if same go straight
        f = open("stuff.txt", "a")
        valuesum = value2 + value
        f.write("value2: " + str(value2) + " value:" + str(value) + "\nSum Value:" + str(valuesum) + "\n")
        f.close()
        # use offset value to change rotations based on value?
        # value , value2 = offset, to be used on degrees turned?
        #
        # 5 + (20 * valuedesc)
        valuedif = abs(value - value2)
        # margin of error allowed
        if valuedif < 0.2:
            return
        if value2 > value:
            # fixed 20 degree rotation
            valuedesc = value2 / valuesum
            drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), 20)
        elif value == value2:
            return
        else:
            valuedesc = value / valuesum
            drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), 20)

    # Movement actions
    def light_transition_model(self, num_of_readings):
        # get average of X number of light intensity readingss

        light_level = 0
        for _ in range(num_of_readings):
            light_level = light_level + cs.reflected_light_intensity
        light_level = light_level / num_of_readings
        print(light_level)
        # light levels, <15, >45, >20
        if light_level < 15:
            return 'Black'
        elif light_level >= 30:
            return 'White'
        elif light_level > 15:
            return 'Gray'

    def left90(self):
        drive.on_for_rotations(-13, 13, 0.95 / 2)
        if self.current_travel_direction == 'Horizontal':
            self.current_travel_direction = 'Vertical'
        else:
            self.current_travel_direction = 'Horizontal'

    def right90(self):
        drive.on_for_rotations(13, -13, 0.95/2)
        if self.current_travel_direction == 'Horizontal':
            self.current_travel_direction = 'Vertical'
        else:
            self.current_travel_direction = 'Horizontal'


