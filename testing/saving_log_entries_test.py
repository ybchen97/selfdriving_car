import numpy as np
from pygame import *
from udp_driving_client import key_handler
from datetime import datetime


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


# initializing pygame
init()
key.set_repeat(1, 500)

screen = display.set_mode((200, 200))
display.set_caption('UDP Server Driving Client (test)')

log = CommandLog()
required_commands = ['f', 'b', 'l', 'r']

while True:
    new_command = key_handler()
    print(new_command)
    if new_command in required_commands:
        new_row = command_to_np(new_command)
        print('new row:', new_row)
        log.add_entries(new_row)
        print('current log:', log.get_log())

    elif new_command == 'esc':
        break


print(log.get_log())

np.savetxt('command_log.txt', log.get_log(), fmt='%s', delimiter=',')
