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
        for light in self.lights:
            self.lights[light].on()
        sleep(1)
        self.lights_out()

    def lights_out(self) -> None:
        for light in self.lights:
            self.lights[light].off()

    def set_led_output(self) -> None:
        # Turn all lights off
        self.lights_out()
        # We'll use F after all
        led = None
        if self.temp_in_f <= 32:
            led = "blue"
        elif 32 < self.temp_in_f <= 70:
            led = "yellow"
        else:
            led = "red"
        self.lights[led].on()

    def calculate_temps(self, voltage: float) -> None:
        self.convert_temp_to_c(voltage)
        self.convert_temp_to_f()

    def convert_temp_to_c(self, voltage: float) -> None:
        self.temp_in_c = 27 - (voltage - 0.706) / 0.001721

    def convert_temp_to_f(self) -> None:
        self.temp_in_f = (self.temp_in_c * 9/5) + 32