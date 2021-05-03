import serial
import pygame
from time import sleep

def press_center():
    print('center')
    global is_play
    if is_play:
        m.pause()
        is_play = 0
    else:
        m.unpause()
        is_play = 1

def press_prev():
    print('prev')
    global current_file
    current_file = (current_file + 2) % num_of_file
    load_new_file()

def press_forw():
    print('forw')
    global current_file
    current_file = (current_file + 1) % num_of_file
    load_new_file()

def press_volume():
    global vol
    for i in range(5):
        if c2 == VOL[i]:
            vol = i
            m.set_volume(vol/6)
            break
    #print('vol')
    print(vol)

def load_new_file():
    global is_play
    print(current_file)
    m.stop()
    #m.unload()
    m.load(file[current_file])
    m.play()
    is_play = 1


START = bytes.fromhex('F2')
END = bytes.fromhex('2F')
CENTER = b'\x84'
PREV = b'\x81'
FORW = b'\x82'
VOL = [b'\x01', b'\x03',b'\x07',b'\x0f',b'\x1f',b'\x1f']
#VOL2 = [bytes.fromhex('80012f'), bytes.fromhex('80032f'), bytes.fromhex('80072f'),bytes.fromhex('800f2f'), bytes.fromhex('801f2f'), bytes.fromhex('803f2f')]
c = ''
c_prev = ''
vol = 6
is_play = 1

file = ["/home/pi/Desktop/audio-stream/music/1.wav","/home/pi/Desktop/audio-stream/music/2.wav"]
num_of_file = len(file)
current_file = 0
pygame.mixer.init()
pygame.mixer.music.load(file[current_file])
m = pygame.mixer.music
m.set_volume(vol/6)
m.play()

ser = serial.Serial("/dev/ttyUSB0",9600)
ser.reset_input_buffer()

while True:
    if ser.inWaiting() > 3:
        first = ser.read()
        if first == START:
            temp = ser.read()
            c_prev = c
            c = temp
            c2 = ser.read()
            if c == CENTER and c_prev != CENTER:
                press_center()
            elif c == PREV and c_prev != PREV:
                press_prev()
            elif c == FORW and c_prev != FORW:
                press_forw()
            elif c != '' and c2 != '':
                press_volume()

    

        
