from time import sleep
from machine import Pin
from Sensor import Sensor
from Thermometer import Thermometer

def main():
    sensor = Sensor()
    thermo = Thermometer()
    thermo.reset()
    power_off = Pin(15, Pin.IN, Pin.PULL_UP)
    while power_off.value() != 0:
        voltage = sensor.read_sensor_voltage()
        thermo.calculate_temps(voltage)
    thermo.reset()

if __name__ == "__main__":
    main()