import RPi.GPIO as GPIO
from time import sleep

INTERVAL = 5
ledpin = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin, GPIO.OUT)

try:
	while True:
		GPIO.output(ledpin, 1)
		sleep(INTERVAL)
		GPIO.output(ledpin, 0)
		sleep(INTERVAL)
except KeyboardInterrupt:
	GPIO.cleanup()
