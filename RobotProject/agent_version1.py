#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, TouchSensor, UltrasonicSensor
from Goal_framework import GoalAgent
import time



speaker = Sound()
mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
cs = ColorSensor()
ts = TouchSensor()
us = UltrasonicSensor()
us.mode = 'US_SI_CM'
drive = MoveTank(OUTPUT_B, OUTPUT_C)
#global
turn_left_on_grey = False
ga = GoalAgent()
vert = False
distance = []
#ga.move('spin', 10, 10, 1)



#the first turn to go towards the bottle
def turn_one(light1):
        global vert
        global count

        print("s " + str(light1) + " " + str(count))#print my info

        drive.off()#stop
        ga.var_forward(0.45)
        time.sleep(1)#waits

        ga.right90()# turn 90 degs to the right
        #count = count + 15
        vert = True


# go forward, and check for tiles
def go(light1,flip1):
    global count
    global vert
    print("e " + str(light1) + " "+str(count))
    # drive.off()ssss
    # time.sleep(.5)sss

    # if we have changed from white to black increase and say count
    if flip1:
        count += 1

        if vert:# check if we are going vericaly as count will need to be increamented by a larger amountssssss
            count += 14
        drive.off()
        #time.sleep(2)
        speaker.speak(str(count))
        #drive.on()

    if count == 56:
        quit()#exit once at square 56
    return not flip1

#method too turn off the grey
def grey_correction (light1,turn_left_on_grey1):
    global count
    print("y " + str(light1) + " " + str(count))
    drive.off()
    time.sleep(.5)

    if turn_left_on_grey1:#check which way we turned last time and turn the other way
        ga.right9()

    else:
        ga.left9()
    return not turn_left_on_grey1 # return which way to turn next time

def find_bottle_with_list():
    check = 0
    global flip
    distance.append(us.distance_centimeters)
    ga.left90()
    if check<2 and flip:
        check += 1
    else:
        drive.off()
        find_bottle_with_list()

#move onto black from startsss
ga.var_forward(0.85)
ga.right90()

#main loop
index = 0 # counter to keep track of the number of times loops runs. Used to get averages of cs.reflected_light_intensity
light = 0 # a var to store these averagess
count = 0
flip = True

while True:

    #update light
    index += 1#
    light += cs.reflected_light_intensity

    if index % 10 == 0:#every 10 times do this block
        light = light / 10# divide light by 10 to get the current average

        if ts.is_pressed:#not my code needs to be commeted :s)
            drive.off()
            break
        if vert:
            drive.on(SpeedPercent(20), SpeedPercent(20))#go forwards
        else:
            drive.on(SpeedPercent(20), SpeedPercent(19.9))
        if count == 11 and not vert:# check if we have moved 11 squares forward
            turn_one(light)


        elif (light < 15 and flip) or ((light > 45 and not flip)and not vert) or (light > 20 and not flip): # checking the the light level is below 15 and were on black or if light level is above 45 and we were on white
            flip = go(light,flip)

        elif light > 20 and light < 35 and not vert : # check if light level is between 20 and 35
            turn_left_on_grey = grey_correction(light,turn_left_on_grey)
        light = 0#reset light


