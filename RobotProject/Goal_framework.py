#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor

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
            self.angle = 


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

    def update_state(self, speed1, speed2, rotations, action_type):
        if action_type == 'rotations':
            self.transition_model(speed1, speed2, rotations, action_type)
            print(self.xy)
        elif action_type == 'spin':
            self.transition_model(speed1, speed2, rotations, action_type)
            print(self.angle)


    def move(self, action_type, speed1, speed2, rotations):
        if action_type == 'rotations':
            drive.on_for_rotations(SpeedPercent(speed1), SpeedPercent(speed2), rotations)
            self.update_state(speed1, speed2, rotations, action_type)
        if action_type == 'spin':
            drive.on_for_rotations(SpeedPercent(speed1), SpeedPercent(-speed2), rotations)
            self.update_state(speed1, speed2, rotations, action_type)
