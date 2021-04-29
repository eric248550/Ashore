import pyaudio, sys, socket
#import keyboard

port = 5001
ip = "192.168.43.5"

chunk = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, output = True, frames_per_buffer = chunk)

#Create a socket connection for connecting to the server:
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((ip, port))

while True:
    #Recieve data from the server:
    data = client_socket.recv(1024)
    stream.write(data,chunk)
    
    #client_socket.sendall(stream.read(chunk))

    print(data)
    '''
    if keyboard.is_pressed('q'):
        print('You Pressed A Key!')
        break  # finishing the loop
        socket.close()
    '''
	
socket.close()
