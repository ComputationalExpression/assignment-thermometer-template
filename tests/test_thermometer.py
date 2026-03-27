import random

from machine import Pin, ADC
from unittest.mock import patch
from main import main
from Thermometer import *
from Sensor import *

lights = {
    "red": Pin(18, Pin.OUT),
    "yellow": Pin(17, Pin.OUT),
    "blue": Pin(16, Pin.OUT)
}

def test_read_sensor_voltage():
    sensor = Sensor()
    with patch('random.randint', return_value = 100000):
        voltage = sensor.read_sensor_voltage()
    assert round(voltage, 2) == 5.04

def test_led_output_hot(capsys):
    thermo = Thermometer()
    thermo.temp_in_f = 71
    thermo.set_led_output()
    out, err = capsys.readouterr()
    assert out == "18 1\n17 1\n16 1\n18 0\n"

def test_led_output_warm(capsys):
    thermo = Thermometer()
    thermo.temp_in_f= 50
    thermo.set_led_output()
    out, err = capsys.readouterr()
    assert out == "18 1\n17 1\n16 1\n17 0\n"

def test_led_output_cold(capsys):
    thermo = Thermometer()
    thermo.temp_in_f = -10
    thermo.set_led_output()
    out, err = capsys.readouterr()
    assert out == "18 1\n17 1\n16 1\n16 0\n"

def test_convert_to_c():
    thermo = Thermometer()
    voltage = random.random()
    v_to_celsius = 27 - (voltage - 0.706) / 0.001721
    thermo.calculate_temps(voltage)
    assert f"{thermo.temp_in_c:.2f}" == f"{v_to_celsius:.2f}"

def test_convert_to_f():
    thermo = Thermometer()
    random_c  = random.randint(-100, 100)
    calculated_f = (random_c * 9/5) + 32
    thermo.temp_in_c = random_c
    thermo.convert_temp_to_f()
    assert f"{thermo.temp_in_f:.2f}" == f"{calculated_f:.2f}"

def test_reset_system(capsys):
    thermo = Thermometer()
    thermo.reset()
    out, err = capsys.readouterr()
    assert out == "18 0\n17 0\n16 0\n18 1\n17 1\n16 1\n"

def test_reset_lights(capsys):
    thermo = Thermometer()
    thermo.lights_out()
    out, err = capsys.readouterr()
    assert out == "18 1\n17 1\n16 1\n"

def test_main_exec_no_err(capsys):
    main()
    out, err = capsys.readouterr()
    assert err == ''
    