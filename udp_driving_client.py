# client for the udp server

import socket
from pygame import *


def key_handler():
    """
    This function handles arrow key keyboard inputs and returns the appropriate commands

    :return:
    Command:
        f: Forward
        b: Backward
        l: Left
        r: Right
        sd: Stop moving
        ss: Stop steering
    """

    run_program = True
    while run_program:
        for e in event.get():
            if e.type == QUIT:  # to make sure the the 'x' button on the window works lol
                run_program = False

            if e.type == KEYDOWN:
                if e.key == K_UP:
                    print('Forward')
                    command = 'f'
                    return command

                elif e.key == K_DOWN:
                    print('Backward')
                    command = 'b'
                    return command

                elif e.key == K_LEFT:
                    print('Left')
                    command = 'l'
                    return command

                elif e.key == K_RIGHT:
                    print('Right')
                    command = 'r'
                    return command

                elif e.key == K_ESCAPE:
                    run_program = False

                else:
                    print('Error -- wrong key pressed. Only press arrow keys.')

            elif e.type == KEYUP:
                if e.key == K_UP or e.key == K_DOWN:
                    print('Stop moving')
                    command = 'sm'
                    return command

                elif e.key == K_LEFT or e.key == K_RIGHT:
                    print('Stop steering')
                    command = 'ss'
                    return command


def main():
    host = '192.168.1.74'
    port = 5001

    server = ('192.168.1.95', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))a

    # initializing pygame
    init()
    key.set_repeat(1, 100)

    screen = display.set_mode((200, 200))
    display.set_caption('UDP Server Driving Client (test)')

    # configuring messages to server
    while True:
        try:
            s.sendto(key_handler().encode('utf-8'), server)
        except AttributeError:
            break

    print('Telling server to close.')
    s.sendto('quit'.encode('utf-8'), server)
    print('Socket closing.')
    s.close()


if __name__ == '__main__':
    main()
