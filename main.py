from Adafruit_SHT31 import *

sensor = SHT31(address=0x44)


def main():
    degrees = sensor.read_temperature()
    humidity = sensor.read_humidity()
    print('Temp             = {0:0.3f} deg C'.format(degrees))
    print('Humidity         = {0:0.2f} %'.format(humidity))


if __name__ == '__main__':
    main()
