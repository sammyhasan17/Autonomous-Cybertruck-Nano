from gpiozero import AngularServo
from time import sleep, time

servo = AngularServo(
    14,
    min_pulse_width=0.0006,
    max_pulse_width=0.0023
)

start_time = time()
DURATION = 15  # seconds

try:
    while time() - start_time < DURATION:
        servo.angle = 0
        sleep(2)

        servo.angle = 90
        sleep(2)

        servo.angle = -90
        sleep(2)

finally:
    servo.angle = None   # stop sending pulses
    servo.close()
    print("Program finished after 15 seconds")
