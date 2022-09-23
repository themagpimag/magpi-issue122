from machine import Pin, PWM
from utime import sleep

# Set PWM pins to control R, G, and B LEDs
pwm13 = machine.PWM(machine.Pin(13))
pwm14 = machine.PWM(machine.Pin(14))
pwm15 = machine.PWM(machine.Pin(15))
pwm13.freq(1000)
pwm14.freq(1000)
pwm15.freq(1000)

# Loop to light R, G, B LEDs in turn
while True:
    # Red
    pwm13.duty_u16(65535)
    sleep(1)
    pwm13.duty_u16(0)
    sleep(1)
    # Green
    pwm14.duty_u16(65535)
    sleep(1)
    pwm14.duty_u16(0)
    sleep(1)
    # Blue
    pwm15.duty_u16(65535)
    sleep(1)
    pwm15.duty_u16(0)
    sleep(1)

