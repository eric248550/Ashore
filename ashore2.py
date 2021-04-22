import serial
from time import sleep


START = bytes.fromhex('F2')
END = bytes.fromhex('2F')
CENTER = bytes.fromhex('84072f')
PREV = bytes.fromhex('813f2f')
FORW = bytes.fromhex('823f2f')
VOL0 = bytes.fromhex('')
VOL1 = bytes.fromhex('80012f')
VOL2 = bytes.fromhex('80032f')
VOL3 = bytes.fromhex('80072f')
VOL4 = bytes.fromhex('800f2f')
VOL5 = bytes.fromhex('801f2f')
VOL6 = bytes.fromhex('803f2f')
c = ''


ser = serial.Serial("/dev/ttyUSB0",9600)
print(ser)
ser.reset_input_buffer()
print("start")

while True:
    if ser.inWaiting() > 3:
        first = ser.read()
        if first == START:
            print("here")
            # record
            temp = ser.read_until(END)
            print(temp.hex())
            c = temp
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

    # debounce
