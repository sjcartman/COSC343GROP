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
    """The class for all goal agent methods and attributes."""
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
        self.max1 = 2
        self.max2 = 2

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

    def correction_sam_main(self, count):
        if count <= 1:
            return
        # move forward to be more on the tile only if not going verts
        # start the timer
        self.var_forward(0.05)
        start_time = time.time()
        while True:
            # move left(because right wheel is turned on)s
            mRight.on(SpeedPercent(20))
            # if light reflected is not blacks
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
        if value > self.max1:
            self.max1 = value
        if value2 > self.max2:
            self.max2 = value2
        value2 = float("{:.2f}".format(value2))
        value = float("{:.2f}".format(value))
        f = open("stuff.txt", "a")
        valuedif = float("{:.2f}".format(abs(value - value2)))#should i use margin of errorsss?
        """ this too """
        if valuedif < 0.4:
            return
        if valuedif < 0.2 and not self.vert:
            return
        f.write("Count : "
                + str(count)
                + "\t"
                + "value: "
                + str(value)
                + "\t"
                + " value2: "
                + str(value2)
                + "\tSum Diff: "
                + str(valuedif))
        # use offset value to change rotations based on value?s
        # value , value2 = offset, to be used on degrees turned?ss
        const_below = 0.4  # if value is less than this, its too close to one side, so turn more
        """ to fix the errors, change the values here """
        if self.vert:  #something to add here to fix the turn
            val = 5  # base value of degrees turned
            if value2 <= const_below or value <= const_below:
                val += 7  # turn more if too close to one side
        else:
            val = 10
            if value2 <= const_below or value <= const_below:
                val += 10  # turn more if too close to one sides
        # margin of error allowed, smaller margin of error means turns less, bigger means turns moressssss
        if value2 > value:
            #convert to log scales
           #val = 10 * math.log10(val)ss
            drive.on_for_degrees(SpeedPercent(20), SpeedPercent(-20), val * value2/self.max2)
            f.write("\nValue2 is more than Value, turn right by " + str(val * value2/self.max2) + "\n")
        elif value == value2:
            return
        else:
            drive.on_for_degrees(SpeedPercent(-20), SpeedPercent(20), val * value/self.max1)
            f.write("\nValue1 is more than Value2, turn left by " + str(val * value/self.max1) + "\n")
        f.close()

    def taya_correction(self, c_value, direction=1):
        drive.on(20, 20)
        start_time = time.time()
        while True:
            test_time = time.time()
            test_total = test_time - start_time
            if cs.reflected_light_intensity < 15 and test_total < 2.8:
                drive.on_for_seconds(-20, -20, 1)
                break
            elif test_total > 2.8:
                drive.off()
                # go back
                drive.on_for_seconds(-20, -20, test_total)
                if direction == 1:
                    drive.on_for_degrees(20, -20, c_value)
                    self.taya_correction(c_value + 5, direction=0)
                    break
                else:
                    drive.on_for_degrees(20, -20, c_value * 2)
                    self.taya_correction(c_value, direction=1)
                    break







