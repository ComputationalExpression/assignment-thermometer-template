from time import sleep
from machine import Pin

class Thermometer:

    def __init__(self):
        self.lights = {
            "red": Pin(18, Pin.OUT),
            "yellow": Pin(17, Pin.OUT),
            "blue": Pin(16, Pin.OUT),
        }

    def reset(self) -> None:
        """
        Reset the thermometer's lights sequence.
        """
        # TODO
        pass

    def lights_out(self) -> None:
        """
        Turn all lights in self.lights off.
        """
        # TODO
        pass

    def set_led_output(self) -> None:
        """
        Set the LED output based on the current temperature in Fahrenheit.
        """
        # TODO
        pass

    def convert_temp_to_c(self, voltage: float) -> None:
        """
        Convert the voltage reading from the temperature sensor to Celsius and store it in self.temp_in_c."""
        # TODO
        pass

    def convert_temp_to_f(self) -> None:
        """
        Convert the temperature in Celsius to Fahrenheit and store it in self.temp_in_f.
        """
        # TODO
        pass
