import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # set the pin numbering mode to BCM
fan_pin = 18 # choose the GPIO pin to control the fan
GPIO.setup(fan_pin, GPIO.OUT) # set the pin as an output

# Define different fan speeds and durations in seconds
fan_speeds = [25, 50, 75, 100] # duty cycles
fan_durations = [10, 20, 30] # seconds

pwm = GPIO.PWM(fan_pin, 50) # create a PWM instance with a frequency of 50Hz
pwm.start(0) # start the PWM with a duty cycle of 0 (off)

try:
    for duration in fan_durations:
        for speed in fan_speeds:
            print("Fan running at {}% for {} seconds".format(speed, duration))
            pwm.ChangeDutyCycle(speed)
            time.sleep(duration)
except KeyboardInterrupt:
    pass

pwm.stop() # stop the PWM
GPIO.cleanup() # clean up the GPIO pins
