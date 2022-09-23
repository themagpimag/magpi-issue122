import anvil.pico
import uasyncio as a
from machine import Pin, PWM

UPLINK_KEY = "<put your Uplink key here>"

# We use the LED to indicate server calls and responses.
led = Pin("LED", Pin.OUT, value=1)

# Set LED levels to zero
redlevel = 0
greenlevel = 0
bluelevel = 0

# Set PWM pins for R, G, and B LEDs
pwm13 = machine.PWM(machine.Pin(13))
pwm14 = machine.PWM(machine.Pin(14))
pwm15 = machine.PWM(machine.Pin(15))
pwm13.freq(1000)
pwm14.freq(1000)
pwm15.freq(1000)

# Red LED control
@anvil.pico.callable_async
async def red(slider):
    redlevel = slider * 256
    pwm13.duty_u16(redlevel)
  
# Green LED control
@anvil.pico.callable_async
async def green(slider):
    bluelevel = slider * 256
    pwm14.duty_u16(bluelevel)

# Blue LED control
@anvil.pico.callable_async
async def blue(slider):
    greenlevel = slider * 256
    pwm15.duty_u16(greenlevel)

# Connect the Anvil Uplink. In MicroPython, this call will block forever.
anvil.pico.connect(UPLINK_KEY)