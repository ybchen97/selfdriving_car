import socket


def main():
    host = '192.168.1.74'
    port = 5001

    server = ('192.168.1.95', 5000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input('YB: ')
    while message != 'q':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('Received from server: ' + data)
        message = input('YB: ')

    s.close()


if __name__ == '__main__':
    main()
