import pyaudio, sys, socket
import wave
import pygame

port = 5001
ip = "192.168.43.5"

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

while True:
    #try:
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
            m = pygame.mixer.music
            m.play()

            file_order+=1

    #print(data)
    #except Exception as e:
     #   print(e)
	
socket.close()
