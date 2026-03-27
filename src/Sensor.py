
from machine import ADC
from time import sleep

class Sensor:

    def __init__(self):
        self.thermo = ADC(4)

    def read_sensor_voltage(self):
        adc_value = self.thermo.read_u16()
        voltage = adc_value * (3.3 / 65535)
        return voltage

    