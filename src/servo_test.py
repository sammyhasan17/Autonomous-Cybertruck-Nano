#import libraries
import RPi.GPIO as GPIO
import time

# set GPIO numbering mode
GPIO.setmode(GPIO.BOARD)

# set pin 11 as an output, set sero_1 as pin 11 as PWM
GPIO.setup(11, GPIO.OUT)
servo_1 = GPIO.PWM(11, 50) # pin 11 at 50Hz frequency

# start PWM running, with value of 0 (pulse off)
servo_1.start(0)
print("Servo test program, wait 2 seconds")
time.sleep

# lets move the servo
print("Rotating 180 degrees in 10  step")
