#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
import time

mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
drive = MoveTank(OUTPUT_B, OUTPUT_C)
cs = ColorSensor()




class GoalAgent:
    """The class for all goal agent methods and attributes."""

    def __init__(self):
        """Initiating method that sets starting position and angle."""
        self.xy = [0, 100]
        self.angle = 90
        self.current_square = None
        self.vert = True

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

    """method to keep the robot straighsssssssssssss
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

    def correction_sam(self):
        value = 0
        value2 = 0
        start_time = time.time()
        while True:
            mRight.on(SpeedPercent(20))
            if cs.color != 1:
                end_time = time.time()
                value = end_time - start_time
                drive.off()
                break
        mRight.on_for_seconds(SpeedPercent(-20), value)
        start_time = time.time()
        while True:
            mLeft.on(SpeedPercent(20))
            if cs.color != 1:
                end_time = time.time()
                value2 = end_time - start_time
                drive.off()
                break
        mLeft.on_for_seconds(SpeedPercent(-20), value2)
        # rotate back based on value2
        if value2 > value:
            drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), 25)
        # turn right? or left, forgot what the speed % was
        elif value == value2:
            return
        # elif value2 == value: go straight
        else:
            drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), 25)
        # else turn left? or right
