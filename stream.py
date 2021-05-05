import serial
import pygame
from time import sleep
import pyaudio, sys, socket
import wave

port = 5001
ip = "192.168.43.144"

chunk = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, output=True, output_device_index=0, frames_per_buffer = chunk)

#Create a socket connection for connecting to the server:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))
# save stream audio
audio_buffer = []
cnt=0
file_order=0
pygame.mixer.init()

def save_wave_file(filename,data):
    wf = wave.open(filename,'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(2)
    wf.setframerate(RATE)
    wf.writeframes(b''.join(data))
    wf.close()

def press_volume():
    global vol
    for i in range(5):
        if c2 == VOL[i]:
            vol = i
            m.set_volume(vol/6)
            break
    #print('vol')
    print(vol)

START = bytes.fromhex('F2')
END = bytes.fromhex('2F')
CENTER = b'\x84'
PREV = b'\x81'
FORW = b'\x82'
VOL = [b'\x01', b'\x03',b'\x07',b'\x0f',b'\x1f',b'\x1f']
c = ''
c_prev = ''
vol = 6
is_play = 1

pygame.mixer.init()
m = pygame.mixer.music
m.set_volume(vol/6)

ser = serial.Serial("/dev/ttyUSB0",9600)
ser.reset_input_buffer()

while True:
    #Recieve data from the server:
    data = client_socket.recv(1024)
    #stream.write(data,chunk) #play stream sound

    audio_buffer.append(data)
    cnt+=1
    #print(cnt)
    if cnt >= 500:
        file_name ='stream_music/' 'stream' + str(file_order) + '.wav'
        save_wave_file(file_name, audio_buffer)
        audio_buffer = []
        cnt=0

        print("Now playing: "+file_name)
        pygame.mixer.music.load(file_name)
        m.play()
        if file_order>=10:
            file_order=0
        else:
            file_order+=1

    if ser.inWaiting() > 3:
        first = ser.read()
        if first == START:
            temp = ser.read()
            c_prev = c
            c = temp
            c2 = ser.read()
            if c != '' and c2 != '':
                press_volume()

    

        
