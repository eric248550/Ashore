import serial
from time import sleep

ser = serial.Serial("/dev/ttyUSB0",9600)
print(ser)
sleep(1)
ser.reset_input_buffer()
print("start")

while True:
	if ser.inWaiting():
		print("!!")
		rec = ser.read(1)
		print(rec)

