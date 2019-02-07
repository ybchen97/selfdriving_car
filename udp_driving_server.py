import socket
import RPi.GPIO as GPIO
import numpy as np
from datetime import datetime


class Motor(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)

        # setting up driving motor
        self.Motor1A = 27
        self.Motor1B = 17
        self.Motor1E = 25

        GPIO.setup(self.Motor1A, GPIO.OUT)
        GPIO.setup(self.Motor1B, GPIO.OUT)
        GPIO.setup(self.Motor1E, GPIO.OUT)

        # setting up steering motor
        self.Motor2A = 14
        self.Motor2B = 15
        self.Motor2E = 18

        GPIO.setup(self.Motor2A, GPIO.OUT)
        GPIO.setup(self.Motor2B, GPIO.OUT)
        GPIO.setup(self.Motor2E, GPIO.OUT)

    def forward(self):
        print('Forward')
        GPIO.output(self.Motor1A, GPIO.HIGH)
        GPIO.output(self.Motor1B, GPIO.LOW)
        GPIO.output(self.Motor1E, GPIO.HIGH)

    def backward(self):
        print('Backward')
        GPIO.output(self.Motor1A, GPIO.LOW)
        GPIO.output(self.Motor1B, GPIO.HIGH)
        GPIO.output(self.Motor1E, GPIO.HIGH)

    def left(self):
        print('Left')
        GPIO.output(self.Motor2A, GPIO.HIGH)
        GPIO.output(self.Motor2B, GPIO.LOW)
        GPIO.output(self.Motor2E, GPIO.HIGH)

    def right(self):
        print('Right')
        GPIO.output(self.Motor2A, GPIO.LOW)
        GPIO.output(self.Motor2B, GPIO.HIGH)
        GPIO.output(self.Motor2E, GPIO.HIGH)

    def stop_moving(self):
        print('Stop moving')
        GPIO.output(self.Motor1E, GPIO.LOW)

    def stop_steering(self):
        print('Stop steering')
        GPIO.output(self.Motor2E, GPIO.LOW)


class CommandLog(object):
    def __init__(self):
        self.log = np.array(['command', 'timestamp']).reshape((1, 2))

    def get_log(self):
        return np.copy(self.log)

    def add_entries(self, row):
        self.log = np.vstack((self.log, row))


def command_to_np(command):
    # creating the row to add
    if command != 'sm' and 'ss':
        timestamp = datetime.now()
        row = np.array([command, timestamp]).reshape((1, 2))
        return row


def command_handler(motor, command):

    if command == 'f':
        motor.forward()

    elif command == 'b':
        motor.backward()

    elif command == 'l':
        motor.left()

    elif command == 'r':
        motor.right()

    elif command == 'sm':
        motor.stop_moving()

    elif command == 'ss':
        motor.stop_steering()


def server_start(log):
    host = '192.168.1.95'
    port = 5000

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print('Server started.')

    required_commands = ['f', 'b', 'l', 'r']

    while True:
        data, addr = s.recvfrom(1024)
        new_command = data.decode('utf-8')

        # Send the command to drive motor
        command_handler(car1, new_command)

        # Append the command and timestamp into a numpy array
        if new_command in required_commands:
            new_row = command_to_np(new_command)
            log.add_entries(new_row)

        elif new_command == 'quit':
            break

    print('Server closing.')
    s.close()


if __name__ == '__main__':
    # Initializing class objects
    car1 = Motor()
    log = CommandLog()

    # Starting the server
    server_start(log)

    print('Saving log entries')
    np.savetxt('command_log.txt', log.get_log(), fmt='%s', delimiter=',')

    GPIO.cleanup()

