from time import sleep

from gpiozero import Servo
#from gpiozero.pins.pigpio import PiGPIOFactory

#servo = Servo(17, pin_factory=PiGPIOFactory())
servo = Servo(17)


def main():
    while True:
        servo.value = 1.0
        sleep(0.5)
        servo.value = -1.0
        sleep(0.5)

if __name__ == "__main__":
    main()
