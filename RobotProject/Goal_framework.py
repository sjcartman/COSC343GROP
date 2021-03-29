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
    """The class for all goal agent methods and attribusstes."""

    def __init__(self):
        """Initiating method that sets starting position and angle."""
        self.xy = [0, 100]
        self.angle = 90
        self.current_square = None

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
            action = #move to red zoned
            action = #move to red zoned
        else if self.xy = #in red zone:
            action = #search for towerss
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
        drive.on_for_rotations(13, -13, 0.95/2)
        return

    def straight_backward(self,rots):
        drive.on_for_rotations(-10,-10,rots)

    def left90(self):
        drive.on_for_rotations(-13, 13, 0.95 / 2)
        return

        return
    def straight_horizontal_one_tile(self):
        drive.on_for_rotations(20,20,1.18)
    def straight_vertical_one_tile(self):
        drive.on_for_rotations(20,19,0.975)
    def var_forward(self, value):
        drive.on_for_rotations(20,20,value)
    def Straighen(self):
        import time
        #check the time too find the line on one side
        time1_start = time.time()
        time1_end = time.time()

        #checkss
        time2_start = time.time()
        time2_end = time.time()

        drive.on(10, -10)
        flopper = False

        while(True):

            if cs.reflected_light_intensity > 20 and cs.reflected_light_intensity < 40 and not flopper:
                import time
                time1_end = time.time()
                drive.off()
                time.sleep(1)
                flopper = True
                drive.on(-10,10)
                time.sleep(0.1)
                time2_start = time.time()
            elif cs.reflected_light_intensity > 20 and cs.reflected_light_intensity < 40 and flopper:
                drive.off()
                time2_end = time1_end
                time.sleep(0.1)

        drive.on(10, -10)
        time1 = time1_end - time1_start
        time2 = time2_end - time1_start

        time = time2 + (time1 * 2)
        time = time/4
        time3_start = time.time()

        while(True):
            time3_end = time.time() - time3_start
            if(time3_end >= time):
                drive.off
                break









