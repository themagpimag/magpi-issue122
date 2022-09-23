# Code for electronics in a ghost busting hoover

import board
import digitalio
import neopixel
from adafruit_led_animation.animation.solid import Solid
from adafruit_led_animation.animation.chase import Chase
from adafruit_led_animation.animation.comet import Comet
from adafruit_led_animation.animation.pulse import Pulse
import pwmio
from adafruit_motor import motor

# Trigger

trigger = digitalio.DigitalInOut(board.GP18)
trigger.switch_to_input(pull=digitalio.Pull.UP)

# LEDs in the handle, GPIO pin they're connected to , number of LEDs

handle = neopixel.NeoPixel(board.GP16, 6)
handle.brightness = 1

# Animation of handle lights

handle_idle = Comet(handle, speed=0.2, color=(0,255,0), tail_length=5)
handle_active = Comet(handle, speed=0.05, color=(0,255,0), tail_length=5)

# LEDs in the wheels

wheels = neopixel.NeoPixel(board.GP0, 16)
wheels.brightness = 0.75

# Animation of wheel during trigger activation

wheels_idle = Solid(wheels, color=(0,255,0))
#wheels_active = Comet(wheels, speed=0.1, color=(0,255,0), tail_length=10)
wheels_active = Chase(wheels, speed=0.1, color=(0,255,0), size=2, spacing=2)

# LEDs in the tank

tank = neopixel.NeoPixel(board.GP28, 15)
tank.brightness = 0.5

# Tank lights animation

tank_pulse = Pulse(tank, speed=0.1, color=(0,255,00))

# Fan motor set up

PWM_PIN_A = board.GP10  # pick any pwm pins on their own channels
PWM_PIN_B = board.GP11

pwm_a = pwmio.PWMOut(PWM_PIN_A, frequency=50)
pwm_b = pwmio.PWMOut(PWM_PIN_B, frequency=50)
fan = motor.DCMotor(pwm_a, pwm_b)

# Main loop

while True:
    tank_pulse.animate()
    if trigger.value:
        #fan.throttle = None
        handle_idle.animate()
        wheels_idle.animate()
    else:
        handle_active.animate()
        wheels_active.animate()
        #fan.throttle = 0.2