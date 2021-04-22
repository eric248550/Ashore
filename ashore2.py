import serial
from time import sleep


START = bytes.fromhex('F2')
END = bytes.fromhex('2F')
CENTER = bytes.fromhex('')
PREV = bytes.fromhex('')
FORW = bytes.fromhex('')
# volume?
c = ''


ser = serial.Serial("/dev/ttyUSB0",9600)
print(ser)
ser.reset_input_buffer()
print("start")

while True:
	if ser.inWaiting() > 3:
		first = ser.read()
        if first == START:
            # record
            temp = ser.read_until(END)
            
        # passng on
        # else:
        #    ser.read_until(END)
        else:
            c = ''
    if c == CENTER:
        print("center")
    elif c == PREV:
        print("prev")
    elif c == FORW:
        print("forw")
    else
        print("n/a")

    # debounce