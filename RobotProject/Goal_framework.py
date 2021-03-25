#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor
import time
#s
mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
drive = MoveTank(OUTPUT_B, OUTPUT_C)


class GoalAgent:
    """The class for all goal agent methods and attributes."""

    def __init__(self):
        """Initiating method that sets starting position and angle."""
        self.xy = [0, 100]
        self.angle = 90
        self.current_square = None

    def transition_model(self, speed1, speed2, rotation, action_type):
        """Transition model method that updates state values based on actions performed."""
        # Note that updating is not instant, but each action should be done with a small time step to make it seem so.
        # Placeholder algorithm values.
        if action_type == 'rotations':
            self.xy[0] = rotation * 2
        elif action_type == 'spin':
            if speed1 > 0:
                self.angle = (self.angle + rotation) % 360
            else:
                self.angle = (self.angle - rotation)

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
        action_list.append(action_step)ssss"""

    def update_state(self, speed1, speed2, rotations, action_type):
        if action_type == 'rotations':
            self.transition_model(speed1, speed2, rotations, action_type)
            print(self.xy)
        elif action_type == 'spin':
            self.transition_model(speed1, speed2, rotations, action_type)
            print(self.angle)


    def move(self, action_type, speed1, speed2 = 1, rotations = 1, rotation_angle=None):
        if action_type == 'rotations':
            drive.on_for_rotations(SpeedPercent(speed1), SpeedPercent(speed2), rotations)
            self.update_state(speed1, speed2, rotations, action_type)
        if action_type == 'spin':
            drive.on_for_rotations(SpeedPercent(speed1), SpeedPercent(-speed1), rotations)
            self.update_state(speed1, speed2, rotations, action_type)
        #if action_type == 'rotate_for':sssss

    def right9(self):
        drive.on_for_rotations(13, 0, 0.095)
        #self.straight_backward(0.525)
        return
    def left9(self):
        drive.on_for_rotations(0, 13, 0.095)
        #self.straight_backward(0.525)
        return


    def right90(self):
        drive.on_for_rotations(13, -13, 0.95/2)
        self.straight_backward(0.525)
        return

    def straight_backward(self,rots):
        drive.on_for_rotations(-10,-10,rots)

    def left90(self):
        drive.on_for_rotations(0, 13, 0.95)
        self.straight_backward(0.525)

        return
    def straight_horizontal_one_tile(self):
        drive.on_for_rotations(20,20,1.18)
    def straight_vertical_one_tile(self):
        drive.on_for_rotations(20,19,0.975)
    def var_forward(self, value):
        drive.on_for_rotations(20,20,value)




