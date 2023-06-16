import time
import threading

import Adafruit_DHT as dht
import RPi.GPIO as GPIO

DHT_PIN = 4
FAN_PIN = 18
SERVO_PIN = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(SERVO_PIN, GPIO.OUT)
GPIO.setup(FAN_PIN, GPIO.OUT)

servo = GPIO.PWM(SERVO_PIN, 50)  # set the PWM frequency to 50Hz
fan = GPIO.PWM(FAN_PIN, 50)


def move_servo():
    servo.start(0)  # start the PWM signal with 0 duty cycle
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


def run_fan():
    fan_speeds = [25, 50, 75, 100]
    duration = 10
    fan.start(0)  # start the PWM with a duty cycle of 0 (off)
    while True:
        for speed in fan_speeds:
            print("Fan running at {}% for {} seconds".format(speed, duration))
            fan.ChangeDutyCycle(speed)
            time.sleep(duration)


def main():
    servo_mover = threading.Thread(target=move_servo, daemon=True)
    fan_runner = threading.Thread(target=run_fan, daemon=True)
    try:
        servo_mover.start()
        fan_runner.start()
        servo_mover.join()
        fan_runner.join()
    except KeyboardInterrupt:
        servo.stop()  # stop the PWM signal on Ctrl-C
        fan.stop()
        GPIO.cleanup()  # clean up the GPIO pins


if __name__ == "__main__":
    main()
