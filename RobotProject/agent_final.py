#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor, TouchSensor
from Goal_framework import GoalAgent
import time

mLeft = LargeMotor(OUTPUT_B)
mRight = LargeMotor(OUTPUT_C)
drive = MoveTank(OUTPUT_B, OUTPUT_C)
us = UltrasonicSensor()
cs = ColorSensor()
speaker = Sound()
ts = TouchSensor()
# global
turn_left_on_grey = False
ga = GoalAgent()
atTower = False
move = 0
check = 0
flip = True


# ga.move('spin', 10, 10, 1)


# the first turn to go towards the bottle
def turn_one(light1):
    global count
    print("s " + str(light1) + " " + str(count))  # print my info

    drive.off()  # stop
    ga.var_forward(0.45)
    time.sleep(1)  # waits
    ga.right90()  # turn 90 degs to the right
    # count = count + 15


# go forward, and check for tiles
# once at tile 55,70,85, and 100 it will move to forward into the grey tile
# and starts calling the find_bottle method. Stores the returned value from
# find_bottle method in "tile" variable and use it to check which tile the tower is located.s
def go(light1, flip1):
    global count
    global move
    global atTower

    print("e " + str(light1) + " " + str(count))
    # drive.off()
    # time.sleep(.5)ssaf

    # if we have changed from white to black increase and say countsssss
    if flip1:
        count += 1

        if ga.vert:  # check if we are going vertically as count will need to be increamented by a larger amounts
            count += 14
            #speaker.speak(str(count))
            #ga.correction_sam_main(0.4)
            #ga.taya_correction(5)
            #drive.on_for_rotations(-20, -20, 1.7)
        drive.off()
        ga.correction_sam_main(count)
        speaker.speak(str(count))
        #ga.center_on_tile(count) put this back if it fucks ups
        #ga.correction(120, count)sss
        time.sleep(1)
        drive.on(20,20)

        if count == 55 or count == 70 or count == 85 or count == 100:
            tile = 0
            found = False
            drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), 2)# change 2 to 1?s
            drive.off()
            ga.left90()
            drive.off()
            time.sleep(1)
            tile += find_bottle()
            if tile == 0:
                speaker.speak("nothing here")
            else:
                a = True
                if count == 55:
                    speaker.speak("tower at {}".format(str(tile)))
                    found = True
                elif count == 70:
                    if tile == 1:
                        speaker.speak("tower at {}".format(str(4)))
                        found = True
                    elif tile == 2:
                        speaker.speak("tower at {}".format(str(5)))
                        found = True
                    elif tile == 3:
                        speaker.speak("tower at {}".format(str(6)))
                        found = True
                elif count == 85:
                    if tile == 1:
                        speaker.speak("tower at {}".format(str(7)))
                        found = True
                    elif tile == 2:
                        speaker.speak("tower at {}".format(str(8)))
                        found = True
                    elif tile == 3:
                        speaker.speak("tower at {}".format(str(9)))
                        found = True
                elif count == 100:
                    if tile == 1:
                        speaker.speak("tower at {}".format(str(10)))
                        print(10)
                        found = True
                    elif tile == 2:
                        speaker.speak("tower at {}".format(str(11)))
                        print(11)
                        found = True
                    elif tile == 3:
                        speaker.speak("tower at {}".format(str(12)))
                        print(12)
                        found = True

            if found:
                time.sleep(100)
                quit()
            else:
                ga.right90()

    return not flip1


# method to search for the bottlesa
def bottle_search():
    goal = False
    while not goal:
        d1 = us.distance_centimeters
        ga.left90()
        drive.on(SpeedPercent(20), SpeedPercent(20))  # go forward
        if (light < 15 and flip) or ((light > 45 and not flip) and not ga.vert) or ((
                                                                                            light > 20 and not flip) and ga.vert):  # checking the the light level is below 15 and were on black or if light level is above 45 and we were on white
            flip = go(light, flip)


# method too turn off the grey
def grey_correction(light1, turn_left_on_grey1):
    global count
    print("y " + str(light1) + " " + str(count))
    drive.off()
    time.sleep(.5)

    if turn_left_on_grey1:  # check which way we turned last time and turn the other wayss
        ga.right9()

    else:
        ga.left9()
    return not turn_left_on_grey1  # return which way to turn next times

# method that stores the distance read by ultrasonic sensor into a variable "distance"
# variable "distance" is then compared to the distance of each tile from where the robot is
# a max of just 3 tiles where each grey tile is roughly 30cm wide.
# if distance falls between the distance the the location of the tile is stored in result and returned.
def find_bottle():
    result = 0
    distance = us.distance_centimeters
    if distance <= 32:
        result += 1
        print(count)
    elif distance>32 and distance <=64:
        result += 2
        print(count)
    elif distance>64 and distance <=100:
        result += 3
        print(count)
    else:
        result = 0

    return result

def move_to_column(list):
    """approx_max_speed = 1500
    ind = list.index(min(list)) + 1
    dist = min(list)
    bl = 0

    if ind == 3:
        drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), (approx_max_speed * 0.2) / dist)
        quit()
    else:
        ga.right90()
        if bl < ind * 2 and flip:
            bl += 1
        else:
            ga.left90()
            drive.on_for_seconds(SpeedPercent(20), SpeedPercent(20), (approx_max_speed * 0.2) / dist)ss
            quit()"""

# move onto black from startsssssssssssss
ga.var_forward(0.85)
ga.right90()

# main loop
index = 0  # counter to keep track of the number of times loops runs. Used to get  averages of cs.reflected_light_intensityss
light = 0  # a var to store these averagesss
count = 0
global flip

while True:
    """change gray correction back.s"""
    # update light
    index += 1
    light = cs.reflected_light_intensity
    # if index % 10 == 0:#every 10 times do this blocksss
    # light = light / 10# divide light by 10 to get the current averages
    if ts.is_pressed:  # stop if the touch sensor is presseds
        drive.off()
        break
    drive.on(SpeedPercent(20), SpeedPercent(20))  # go forwards

    if count == 10 and not ga.vert:  # check if we have moved 11 squares forward
        turn_one(light)
        ga.correction_sam_main(count)
        #ga.taya_correction(5)



    elif (light < 15 and flip) or ((light > 45 and not flip) and not ga.vert) or ((light > 20 and not flip) and ga.vert):  # checking the the light level is below 15 and were on black or if light level is above 45 and we were on white
        flip = go(light, flip)

ga.move('rotations', 10, 10, 1.5)





