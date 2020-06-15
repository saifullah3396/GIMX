import socket
from enum import IntEnum
from time import sleep
import struct
import sys

DEFAULT_IP = "127.0.0.1"
DEFAULT_PORT = 51914


def send_message(ip, port, value):

    packet = bytearray([0x02, value])  # type + value
    print("Sending packet: {0}".format(packet))

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(packet, (ip, port))



def check_status(ip, port):

    packet = bytearray([0x00, 0x00])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((ip, port))
    sock.send(packet)
    timeval = struct.pack('ll', 1, 0)  # seconds and microseconds
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVTIMEO, timeval)
    try:
        data, (address, port) = sock.recvfrom(2)
        response = bytearray(data)
        if (response[0] != 0x00):
            print("Invalid reply code: {0}".format(response[0]))
            return 1
    except socket.error as err:
        print(err)

    return 0


def main():

    ip = DEFAULT_IP
    port = DEFAULT_PORT

    if check_status(ip, port):
        sys.exit(-1)

    send_message(ip, port, 1)
    sleep(1)


if __name__ == "__main__":
    main()

