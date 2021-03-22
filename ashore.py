import gpiozero as gpio
import serial
import pygame
from time import sleep
'''
ser = serial.Serial ("/dev/ttyS0", 9600)
'''
switch = gpio.Button(18)
switch.when_pressed = set_state(1)
switch.when_released = set_state(0)
breathLED = gpio.RGBLED(3,4,5)
motor_relay = gpio.DigitalOutputDevice(6)
is_active = 1

music_state = 0
music_volume = 3 #0-7


def toggle_motor_relay():
    global motor_relay
    if motor_relay.value:
        motor_relay.off()
    else:
        motor_relay.on()

def set_state(val):
    global is_active
    global motor_relay
    state = val
    print(val)
    if val:
        motor_relay.on()
    else:
        motor_relay.off()

def init_player():
    file=r'' # 播放音樂的路徑，從網路上載下來的音檔存放位子
    pygame.mixer.init()
    pygame.mixer.music.load(file)

def center():
    global music_state
    if music_state:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    #todo

def prev():
    #todo
    return 0 

def next():
    #todo
    return 0

def set_volume(vol):
    global music_volume
    music_volume = vol
    #todo


if __name__ == '__main__':
    motor_relay.off()
    print("check")
    try:
        motor_relay.off()
        while True:
            if is_active:
                breathLED.pulse(fade_in_time=5, fade_out_time=5, on_color=(0, 255, 0), off_color=(0, 0, 255))
                '''
                rec = ser.read()
                if rec is 242:
                    data = ''
                    while ser.inWaiting():
                        data += ser.read(data_left)
                    if data is "D3": #todo
                        center()
                    elif data is "D1":
                        next()
                    elif data is "D2":
                        prev()
                    elif data is "D6":
                        set_volume(6)
                    elif data is "D5":
                        set_volume(6)
                    elif data is "D4":
                        set_volume(4)
                    elif data is "D3":
                        set_volume(3)
                    elif data is "D2":
                        set_volume(2)
                    elif data is "D1":
                        set_volume(1)
                '''
            sleep(1)

    except (GPIOZeroError,KeyboardInterrupt):
        ser.close()
        print("close")