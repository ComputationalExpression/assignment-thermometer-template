
from machine import ADC
from time import sleep

class Sensor:

    def __init__(self):
        self.thermo = ADC(4)

    def read_sensor_voltage(self):
        """Read the 16-bit ADC value from the temperature sensor and convert it to volts.

        This method calls self.thermo.read_u16() to obtain a 16-bit ADC reading
        (0–65535) and converts it to a voltage using a 3.3V reference.

        Returns:
            float: The measured voltage in volts.
        """
        # TODO - Implement the method to read the ADC value and convert it to voltage
    
