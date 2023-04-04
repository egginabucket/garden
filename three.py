import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)  # set the mode to use physical pin numbering
GPIO.setup(11, GPIO.OUT)  # set up GPIO pin 11 to control the servo
servo = GPIO.PWM(11, 50)  # set the PWM frequency to 50Hz

servo.start(0)  # start the PWM signal with 0 duty cycle

try:
    while True:
        # smoothly oscillate the servo from 0 to 180 degrees
        for angle in range(0, 181, 1):
            duty = angle / 18 + 2
            servo.ChangeDutyCycle(duty)  # set the duty cycle to move the servo
            time.sleep(0.02)  # wait for the servo to reach the position
        for angle in range(180, -1, -1):
            duty = angle / 18 + 2
            servo.ChangeDutyCycle(duty)  # set the duty cycle to move the servo
            time.sleep(0.02)  # wait for the servo to reach the position

except KeyboardInterrupt:
    servo.stop()  # stop the PWM signal on Ctrl-C
    GPIO.cleanup()  # clean up the GPIO pins
