#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor,TouchSensor
from Goal_framework import GoalAgent
import time


mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
drive = MoveTank(OUTPUT_B, OUTPUT_C)
us = UltrasonicSensor()
cs = ColorSensor()
speaker = Sound()
ts = TouchSensor()
#global
turn_left_on_grey = False
ga = GoalAgent()
vert = False
atTower = False
distance = []
move = 0
check = 0
flip = True
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
    global move
    global atTower

    print("e " + str(light1) + " "+str(count))
    # drive.off()ssss
    # time.sleep(.5)sss

    # if we have changed from white to black increase and say count
    if flip1:
        count += 1

        if vert: # check if we are going vertically as count will need to be increamented by a larger amountssssss
            count += 14
        drive.off()
        #time.sleep(2)
        speaker.speak(str(count))
        #drive.on()

    if count == 56:
        atTower = True

    if atTower:
        #quit()#exit once at square 56
        # quit()#exit once at square 56
        if move < 3:
            find_bottle_with_list()
            move += 1
        else:
            move_to_column(distance)


        drive.off() #Stops at 56
        #bottle_search()

    return not flip1

# method to search for the bottle
def bottle_search():
    goal = False
    while not goal:
        d1 = us.distance_centimeters
        ga.left90()
        drive.on(SpeedPercent(20), SpeedPercent(20))#go forward
        if (light < 15 and flip) or ((light > 45 and not flip)and not vert) or ((light > 20 and not flip)and vert): # checking the the light level is below 15 and were on black or if light level is above 45 and we were on white
            flip = go(light,flip)



#method too turn off the grey
def grey_correction (light1,turn_left_on_grey1):
    global count
    print("y " + str(light1) + " " + str(count))
    drive.off()
    time.sleep(.5)

    if turn_left_on_grey1:#check which way we turned last time and turn the other wayss
        ga.right9()

    else:
        ga.left9()
    return not turn_left_on_grey1 # return which way to turn next times


def find_bottle_with_list():
    global check
    global flip
    global vert
    distance.append(us.distance_centimeters)
    ga.left90()
    vert = not vert
    if check<2 and flip:
        check += 1
    else:
        ga.right90()
        vert = not vert
        drive.off()

def move_to_column(list):
    approx_max_speed = 1500
    ind = list.index(min(list)) + 1
    dist = min(list)
    bl = 0
    global vert

    if ind == 3:
        drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), (approx_max_speed*0.2)/dist)
        quit()
    else:
        ga.right90()
        if bl<ind*2 and flip:
            bl+=1
        else:
            ga.left90()
            vert = not vert
            drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), (approx_max_speed*0.2)/dist)
            quit()

#move onto black from startssss
ga.var_forward(0.85)
ga.right90()

#main loop
index = 0 # counter to keep track of the number of times loops runs. Used to get averages of cs.reflected_light_intensity
light = 0 # a var to store these averages
count = 0
global flip

while True:
    """change gray correction back."""
    #update light
    index += 1
    light = cs.reflected_light_intensity

    #if index % 10 == 0:#every 10 times do this block
    #light = light / 10# divide light by 10 to get the current average

    if ts.is_pressed:#not my code needs to be commeted :)
        drive.off()
        break
    drive.on(SpeedPercent(20), SpeedPercent(19.9))#go forward

    if count == 11 and not vert:# check if we have moved 11 squares forward
        turn_one(light)


    elif (light < 15 and flip) or ((light > 45 and not flip)and not vert) or ((light > 20 and not flip)and vert): # checking the the light level is below 15 and were on black or if light level is above 45 and we were on white
        ga.Straighen()
        flip = go(light,flip)

ga.move('rotations', 10, 10, 1.5)


            


