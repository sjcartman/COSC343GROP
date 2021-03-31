#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
import time
import sys, math

mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
drive = MoveTank(OUTPUT_B, OUTPUT_C)
cs = ColorSensor()



class GoalAgent:
    """The class for all goal agent methods and attributess."""
    def vert(self):
        global vert
        return vert

    def __init__(self):
        """Initiating method that sets starting position and angle."""
        self.xy = [0, 100]
        self.angle = 90
        self.current_square = None
        self.vert = True
        self.correction_filp = True
        self.max1 = 0
        self.max2 = 0
        self.value_difference = 10

    def transition_model(self, speed1, speed2, rotation):
        """Transition model method that updates state values based on actions performed."""
        # Note that updating is not instant, but each action should be done with a small time step to make it seem so.
        # Placeholder algorithm values.
        if self.angle == 90:
            self.xy[0] = rotation*2
        #self.angle = rotation*3.14
        return self.xy

    def xy_square_conversion(self, light_input):
        """Conversion method that converts current xy position to current black square position."""
        square = self.xy[0] + self.xy[1] % 12
        return square

    def sensor_model(self, light_intensity_input):
        """Sensor model method that updates current world state based on agent percepts."""
        # Note that the best sensor model will compare current square values to previous ones.
        # Placeholder algorithm values.
        if light_intensity_input <= 50:
            self.current_square = self.xy[0] + self.xy[1] % 12
        else:
            self.current_square = None

    """def rules(self):
        #Rules method that decides actions based on current world state
        if self.xy = [0, 0]:
            action = #move to red zone
        else if self.xy = #in red zone:
            action = #search for tower
    #
    def action(self, action_step):
        action_list.append(action_step)"""

    def move(self, type, speed1, speed2, rotations):
        if type == "rotations":
            drive.on_for_rotations(SpeedPercent(speed1), SpeedPercent(speed2), rotations)
            self.update_state(speed1, speed2, rotations, action_type)
        if action_type == 'spin':
            drive.on_for_rotations(SpeedPercent(speed1), SpeedPercent(-speed1), rotations)
            self.update_state(speed1, speed2, rotations, action_type)
        #if action_type == 'rotate_for':sssssssssssss

    def right9(self):
        drive.on_for_rotations(13, -13, 0.045/2)
        #self.straight_backward(0.525)
        return

    def left9(self):
        drive.on_for_rotations(-13, 13, 0.045/1.8)
        #self.straight_backward(0.525)ss
        return

    def right90(self):
        self.vert = not self.vert
        drive.on_for_rotations(13, -13, 0.95/2)
        self.max1 = 2
        self.max2 = 2
        return

    def straight_backward(self,rots):
        drive.on_for_rotations(-10,-10,rots)

    def left90(self):
        self.vert = not self.vert
        drive.on_for_rotations(-13, 13, 0.95 / 2)
        return

        return
    def straight_horizontal_one_tile(self):
        drive.on_for_rotations(20,20,1.18)
    def straight_vertical_one_tile(self):
        drive.on_for_rotations(20,19,0.975)
    def var_forward(self, value):
        drive.on_for_rotations(20,20,value)

    def var_backwards(self, value):
        drive.on_for_rotations(-20,-20,value)

    """method to keep the robot straighssssssssssssss
    ss"""
    def correction(self, value, count):
        speed = 13
        if count != 1 :
            #drive.on_for_rotations(20, 20, 0.3)
            time.sleep(0.1)
            drive.on_for_degrees(speed, -speed, value)
            time.sleep(0.1)
            while cs.reflected_light_intensity > 10:
                drive.on(-speed, speed)
            drive.off()
            time.sleep(0.1)
            drive.on_for_degrees(-speed, speed, 2 * value)
            time.sleep(0.1)
            while cs.reflected_light_intensity > 10:
                drive.on(speed, -speed)
            drive.off()
            time.sleep(0.1)
            drive.on_for_degrees(speed, -speed, value)
            time.sleep(0.1)

    def correction_sam(self, count):
        self.correction_filp = True
        self.correction_sam_main(count)

    def correction_sean(self, count):
        self.correction_filp = True
        self.correction_sam_main_sean(count)
    # the base method to record time taken in both directions
    def correction_sam_main1(self, count):
        self.var_forward(0.05)
        start_time = time.time()
        while True:
            # move left(because right wheel is turned on)s
            mRight.on(SpeedPercent(20))
            # if light reflected is not blacks
            if cs.reflected_light_intensity > 20:
                # record the time
                end_time = time.time()
                # save it into a value
                value = end_time - start_time
                # stop the motors
                drive.off()
                sleep(0.1)
                # break out of the surrounding while loop
                break
        # return back to normal position
        mRight.on_for_seconds(SpeedPercent(-20), value)
        # repeat the above for the right(left wheel now turned on)
        start_time = time.time()
        while True:
            mLeft.on(SpeedPercent(20))
            if cs.reflected_light_intensity > 20:
                end_time = time.time()
                value2 = end_time - start_time
                drive.off()
                sleep(0.1)
                break
        mLeft.on_for_seconds(SpeedPercent(-20), value2)
        # if either max1 or max2 has not yet been set, use the current two as the first values
        if self.max1 == 0 or self.max2 == 0:
            self.max1 = value
            self.max2 = value2
            self.value_difference = abs(value - value2)
            return
        # one of these will evaluate to a positive, and the other to a negative. 
        # We want to turn in the direction of the positive, based on the difference between the previous and current value. 
        if (value2 - self.max2) > 0:
            mLeft.on_for_seconds(SpeedPercent(20), value2 - self.max2 * 0.5)
        elif (value - self.max1) > 0:
            mRight.on_for_seconds(SpeedPercent(20), value - self.max1 * 0.5)
        # set the max to the new one (we can implement valuedif such that this only sets if valuedif is smaller than previously).
        if self.value_difference > abs(value-value2):
            self.max1 = value
            self.max2 = value2
            self.value_difference = abs(value-value2)

    def correction_sam_main(self, x):
        if x == 1:
            return
        coef = 0.85
        start_time = time.time()
        while True:
            # move left(because right wheel is turned on)ssss
            mRight.on(SpeedPercent(20))
            # if light reflected is not blackss
            if cs.reflected_light_intensity > 20:
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
        # repeat the above for the right(left wheel now turned on)ssssss
        start_time = time.time()
        while True:
            mLeft.on(SpeedPercent(20))
            if cs.reflected_light_intensity > 20:
                end_time = time.time()
                value2 = end_time - start_time
                drive.off()
                break
        mLeft.on_for_seconds(SpeedPercent(-20), value2)

        cirle_1 = self.time_to_rads(value)
        cirle_2 = self.time_to_rads(value2)

        cirle_3 = abs((cirle_1 - cirle_2)/2)

        cirle_4 = math.atan(cirle_3)
        cirle_5 = self.rad_to_deg(cirle_4)
        #max = 90
        #if cirle_5 > max :s
        #    cirle_5 *= 0.5
        if cirle_1 > cirle_2:
            drive.on_for_degrees(-20, 20, cirle_5 * coef)
        elif cirle_2 > cirle_1:
            drive.on_for_degrees(20, -20, cirle_5 * coef)


    def rad_to_deg(self,rad):
        rad *= 180/math.pi
        return  rad
    def time_to_rads(self,time):
        return time/2.71139001846


    def taya_correction(self, c_value, direction=1):
        while cs.reflected_light_intensity < 15:
            drive.on(20, 20)
        drive.off()
        drive.on_for_rotations(20, 20, 1.85)
        while True:
            if cs.reflected_light_intensity < 15:
                drive.on_for_rotations(-20, -20, -1.7)
                break
            else:
                drive.off()
                drive.on_for_rotations(-20, -20, 1.85)
                if direction == 1:
                    drive.on_for_degrees(20, -20, c_value)
                    self.taya_correction(c_value + 5, direction=0)
                    break
                else:
                    drive.on_for_degrees(-20, 20, c_value)
                    self.taya_correction(c_value + 5, direction=1)
                    break







