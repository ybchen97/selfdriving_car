# import motor
from pygame import *

# from time import sleep
# import RPi.GPIO as GPIO

# setting and initializing motor details
# motor.init()

# initializing pygame
init()

screen = display.set_mode((640, 480))
display.set_caption('The amazing key presser!')

key.set_repeat(1, 100)
run_program = True

while run_program:
    for e in event.get():
        if e.type == QUIT:  # to make sure the the 'x' button on the window works lol
            run_program = False

        if e.type == KEYDOWN:
            if e.key == K_UP:
                # motor.forward()
                print('forward')
            elif e.key == K_DOWN:
                # motor.backward()
                print('backward')
            elif e.key == K_LEFT:
                # motor.left()
                print('left')
            elif e.key == K_RIGHT:
                # motor.right()
                print('right')
            elif e.key == K_ESCAPE:
                run_program = False
            else:
                print('error -- wrong key pressed')

        elif e.type == KEYUP:
            if e.key == K_UP or e.key == K_DOWN:
                # motor.stop_moving()
                print('stop moving')

            elif e.key == K_LEFT or e.key == K_RIGHT:
                # motor.stop_steering()
                print('stop steering')


