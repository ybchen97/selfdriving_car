import RPi.GPIO as GPIO
# from time import sleep


def init():
    GPIO.setmode(GPIO.BCM)

    # setting up driving motor
    Motor1A = 27
    Motor1B = 17
    Motor1E = 25

    GPIO.setup(Motor1A, GPIO.OUT)
    GPIO.setup(Motor1B, GPIO.OUT)
    GPIO.setup(Motor1E, GPIO.OUT)

    # setting up steering motor
    Motor2A = 14
    Motor2B = 15
    Motor2E = 18

    GPIO.setup(Motor2A, GPIO.OUT)
    GPIO.setup(Motor2B, GPIO.OUT)
    GPIO.setup(Motor2E, GPIO.OUT)


def forward():
    print('Forward')

    GPIO.output(Motor1A, GPIO.HIGH)
    GPIO.output(Motor1B, GPIO.LOW)
    GPIO.output(Motor1E, GPIO.HIGH)


def backward():
    print('Backward')
    GPIO.output(Motor1A, GPIO.LOW)
    GPIO.output(Motor1B, GPIO.HIGH)
    GPIO.output(Motor1E, GPIO.HIGH)


def left():
    print('Left')
    GPIO.output(Motor2A, GPIO.HIGH)
    GPIO.output(Motor2B, GPIO.LOW)
    GPIO.output(Motor2E, GPIO.HIGH)


def right():
    print('Right')
    GPIO.output(Motor2A, GPIO.LOW)
    GPIO.output(Motor2B, GPIO.HIGH)
    GPIO.output(Motor2E, GPIO.HIGH)


def stop_moving():
    print('Stop moving')
    GPIO.output(Motor1E, GPIO.LOW)


def stop_steering():
    print('Stop steering')
    GPIO.output(Motor2E, GPIO.LOW)

