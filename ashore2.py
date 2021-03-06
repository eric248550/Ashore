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

def press_forw():
    print('forw')

def press_volume():
    global vol
    for i in range(len(VOL)):
        if c == VOL[i]:
            vol = i+1
            m.set_volume(0.5 + vol/12)
            break
    #print('vol')
    #print(vol)


START = bytes.fromhex('F2')
END = bytes.fromhex('2F')
CENTER = bytes.fromhex('840f2f')
PREV = bytes.fromhex('813f2f')
FORW = bytes.fromhex('823f2f')
VOL = [bytes.fromhex('80012f'), bytes.fromhex('80032f'), bytes.fromhex('80072f'),bytes.fromhex('800f2f'), bytes.fromhex('801f2f'), bytes.fromhex('803f2f')]
'''
VOL1 = bytes.fromhex('80012f')
VOL2 = bytes.fromhex('80032f')
VOL3 = bytes.fromhex('80072f')
VOL4 = bytes.fromhex('800f2f')
VOL5 = bytes.fromhex('801f2f')
VOL6 = bytes.fromhex('803f2f')
'''
c = ''
c_prev = ''
vol = 6
is_play = 1

file = "./music.mp3"
pygame.mixer.init()
pygame.mixer.music.load(file)
m = pygame.mixer.music
m.set_volume(0.5 + vol/12)
m.play()

ser = serial.Serial("/dev/ttyUSB0",9600)
ser.reset_input_buffer()

while True:
    if ser.inWaiting() > 3:
        first = ser.read()
        if first == START:
            temp = ser.read_until(END)
            c_prev = c
            c = temp
        else:
            c = ''
    if c == CENTER and c_prev != CENTER:
        press_center()
    elif c == PREV and c_prev != PREV:
        press_prev()
    elif c == FORW and c_prev != FORW:
        press_forw()
    elif c != '':
        press_volume()
