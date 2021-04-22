import RPi.GPIO as GPIO
from time import sleep
import math

delay = 0.03
middleDelay = 0.5
ledpin = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledpin, GPIO.OUT)

p = GPIO.PWM(ledpin, 5000)
p.start(0)
try:
	while True:
		for dc in range(0,101, 5):
			p.ChangeDutyCycle(dc)
			sleep(delay*(3-dc/100))
		sleep(middleDelay)
		for dc in range(100,-1, -5):
			p.ChangeDutyCycle(dc)
			sleep(delay*(3-dc/100))
		sleep(middleDelay)
except KeyboardInterrupt:
	p.stop()
	GPIO.cleanup()

# set1: 0.05 0.5 delay*(1-dc/100)
