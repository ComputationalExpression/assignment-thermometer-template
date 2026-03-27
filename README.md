# Taking the Temperature

![Image](https://raw.githubusercontent.com/ComputationalExpression/assignment-thermometer-template/refs/heads/media/media/thermometer.png)

|Date |       |
|:----|:------|
|27 March 2026 |Assigned |
|3 April 2026 |Due |
|Progress        |[![Grade](../../actions/workflows/main.yml/badge.svg?branch=main)](../../actions/workflows/main.yml) |

![](https://img.shields.io/badge/assignment-lab-yellow.svg?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAACXBIWXMAAAB2AAAAdgFOeyYIAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAAa9JREFUOI2Vkk1IVGEUhp9zvd7bfKNz51JojQWZkARmI2qCULjrbxkTs4nCVRC0LHeuZhGzDFqEKzcGs2vXxhatAxUhUTQt1I0mNkzZ/NzjYrBmplFu7+bjvOfl4ZyPIzTRtZR2BcKVWs9SPs/nZLMxazcDBBajmQkyXowYwMY2X7OvyAK5UADH4kM0gokbOksBurnNSslltlnWamZ+mpGdwk+KAEGF8uo67tK07IYGAKhU37Ly67jMiYA/ASGSL3DqvwDJxxp3bVoAygE/oobiYEq90AD9TV+snXYAxybm+5QqQl9oQOIs48bBB3BbaL1/iyHP51EoQDKtYy+eckfkrxe1sZ+Mk0ymdexEwEBaEw9TvPQMHVrbELh8nuF7t3k+kNZEbavukEau87q3hzNbu2zs7JH/vkf+XAfexS4uWBbujREuvZ9lCrhbw67q6gO9+SbLO+NQ99sKWiiyXzzgwEQwW/usTWZ4tvBWPtZPYDFoWqu33zC9tDnEcaq130avwhBQDxBhfnGduc7TxBshR6oowfIa36yAuX9WAOhPabcKPccBAERZXcjJl6P6EOkCeLyZu19AAAAAAElFTkSuQmCC)

For this lab, you'll collaborate with a teammate to develop a thermometer using the on-board temperature sensor on the Raspberry Pi Pico. This project should use the LEDs to display the relative warmth (hot, warm, cold) the surrounding environment.

## Learning Objectives

This assignment addresses the following course learning objective(s):

1. Apply Python programming fundamentals to execute and explain computer code that implements interactive, novel solutions to a variety of computable problems.
2. Implement code consistent with industry-standard practices using professional-grade integrated development environments (IDEs), command-line tools, and version control systems.
3. Analyze and suggest revisions to existing Python language code to add functionality or repair defects.
4. Evaluate the practical and ethical implications of writing computer code and discuss the contexts, perceived effects, and impacts exerted on and by computer code as a cultural force or artifact.
5. Design, describe, and implement original projects incorporating industry-standard practices and Python language fundamentals.

## Pinout Diagram

> [!NOTE]
> This is similar to the `Stoplight` lab, with the substitution of a `blue` LED.

![Thermometer Pinout](https://raw.githubusercontent.com/ComputationalExpression/assignment-stoplight-template/refs/heads/media/media/100%20-%20Pico%20(Stoplight).png)

The above graphic is a `pinout diagram`: a description of how to wire a _physical computing_ project. Match the above diagram with the following components:

* push button
* Raspberry Pi Pico
* `2` wires
* breadboard
* `3` resistors
* `3` LEDs

|Pins |Purpose |
|:----|:-------|
|`15` |Button  |
|`16` |Blue light<sup>†</sup> |
|`17` |Yellow light<sup>†</sup> |
|`18` |Red light<sup>†</sup> |

> [!IMPORTANT]
> The above writing is _critical_ to the code. We address specific parts during our programs. Make sure it matches. If you have questions, ask a TL or the instructor!
>
> <sup>†</sup>: indicates that a resistor must exist between the light and the pin.

## Summary of the problem

> [!IMPORTANT]
> In order to run the program in this lab, you'll need to do the following when you've made the appropriate changes:
> ```
> uv run mpremote cp src/Thermometer.py :
> uv run mpremote cp src/Sensor.py :
> ```
> As you will make changes in this file to create a functional `Thermometer` and `Sensor`, you'll need to do this each time the file changes!

> [!NOTE]
> In order to test this lab, you may need to be a bit creative about temperature surrounding the device. However, keep in mind that you _should not_ expose it to open flame or another _very hot_ heatsource (i.e., put it directly in an oven or microwave).
>
> As part of this lab, you'll need to figure out how to test this device!

The lab consists of three (`3`) parts:

* a `Sensor` object which captures the value of the Pico temperature sensor
* a `Thermometer` object that determines relative warmth and displays results using `LEDs`
* a `main` (driver) file that controls the interaction between the `Sensor` and `Thermometer`, while guiding the flow of the program

### `main`

`main` operates a loop until the `power_off` button is pressed, at which time the apparatus turns off. On startup, the `main` should instruct the `Thermometer` to go through the reset cycle described below.

### `Sensor`

This object has one purpose: read the internal sensor. We set this sensor up using the following approach (the necessary imports are already in the file):
```python
ADC(4)
```

One _might_ think that reading a temperature sensor results in a temperature. Here, that's not the case. The sensor reports a relative voltage which we need to calculate using the following formula:

$$ 
reading \times \frac{3.3}{65535} 
$$

This should result from a _method_ of `Sensor` named `read_sensor_voltage` called in `main`.

### `Thermometer`

#### Temperatures

Now that we have the reading of the voltage of the sensor, we convert to a `Celsius` temperature using the following conversion:

$$ 27 - \frac{(voltage - 0.706)}{0.001721} $$

From there, we can calculate the temperature in Fahrenheit, which we'll use to determine relative warmth:

$$ (celsius \times \frac{9}{5}) + 32$$

The functions that do this work should be named, respectively:
* `convert_temp_to_c`
* `convert_temp_to_f`

However, rather than return a value, each should set `properties` of the object called `temp_in_c` and `temp_in_f`. We'll use these to operate the `LED`s. 

#### `LED` control

`LED`s should be controlled using the following functions and approach:
|Function |Description |
|:--------|:-----------|
|`reset`  |Turns all `LED`s on for `1` second, then off |
|`lights_out`|Turns all `LED`s off |
|`set_led_output`|Turns on the appropriate light for temperature conditions (see below) |

This table describes use of the `LED`s:

|`LED`|Designation |Meaning |
|:----|:-------|:-----------|
|`Red`|Hot     |Temperature greater than `70` degrees|
|`Yellow`|Warm |Temperature between `32` and `70` degrees |
|`Blue` |Cold |Temperature lower than `32` degrees |



### Implementing hardware

The hardware (the Raspberry Pi Pico) relies on some fundamental structures:

* `Pin`s
  * `Pin.IN`
  * `Pin.OUT`
* `sleep` 

#### `Pin`s

`Pin`s represent physical pins on the Raspberry Pi Pico device which can be either `input`s or `output`s. Our `button` is an input: `Pin(16, Pin.IN)`; our LED is an on-board output: `Pin("LED", Pin.OUT)`.

As a general rule, `0` indicates a press, and `1` indicates the button is _not_ being pressed.

#### LEDs

`LED`s (lights) required `Pin.OUT` modes. For example, to program the `RED` light. To turn these on and off, use the `on` and `off` methods of the `Pin`.
```python
# Turns light ON
self.lights[light].on()
# Turns light OFF
self.lights[light].off()
```

## Assignment procedure

> [!IMPORTANT]
> As a team assignment, this repository _does not allow_ direct `commit`s to `main`. Here you'll have to use `branch`es and reviews to ensure that the project functions and is generally well understood by the team. 
>
> In practice, this means that everyone _must_ `branch` their changes _and_ that each `Pull Request` requires `2` reviews before it can be `merge`d.

## Evaluation

> [!NOTE]
> To grade this lab, use the `uv run gatorgrade` command.

Labs in this course are each worth `5` points. You are awarded different levels of points using the following rubric:

|Component|Value |
|:--------|:-----|
|Programming|2   |
|Code Review|2   |
|Writing    |1   |
|**Total**  |**5**|

### Programming

Your programming will be evaluated on the following characteristics:

* Program reflects startup expectations in `main`
* Program reads correct temperature
* Program displays relative temperature correctly using `LED`s

#### Expected output

The output for this program relies on external LEDs to validate outputs/outcomes.

#### Code review

Either a Technical Leader `TL` or the instructor can perform a code review with you. This _must_ be done before the due date for the assignment. You may accomplish this during a lab session, TL office hours, or during the instructor's office hours. Successful completion of this review (and an accompanying successful outcome) will earn points toward the code review portion of the assignment.

Even though this assignment is _collaborative_, each student must complete the code review on their own.

#### Writing

Students are expected to finish a [summary document](docs/summary.md). This is a Markdown file containing questions. All questions must be answered fully. Typically, this means a word count is assessed. 

For this assignment, the minimum required word count is `150`.
