import serial
import sys


def run(port) -> None:
    with serial.Serial(port=port, baudrate=115200) as ser:
        while True:
            print(ser.readline())


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Missing required argument: port')
        exit()
    run(sys.argv[1])

