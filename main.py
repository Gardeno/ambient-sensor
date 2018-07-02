from Adafruit_SHT31 import *
from blessings import Terminal
import time

sensor = SHT31(address=0x44)


def main():
    degrees = sensor.read_temperature()
    humidity = sensor.read_humidity()
    print('Temp             = {0:0.3f} deg C'.format(degrees))
    print('Humidity         = {0:0.2f} %'.format(humidity))
	
    t = Terminal()
    with t.fullscreen():
        print t.bold('Hi there!')
        print t.bold_red_on_bright_green('It hurts my eyes!')

        with t.location(0, t.height):
            print 'This is at the bottom.'
        time.sleep(5)


if __name__ == '__main__':
    main()
