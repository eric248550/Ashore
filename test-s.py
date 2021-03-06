import pyaudio, sys, socket

port = 5001
chunk = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, output = True, frames_per_buffer = chunk)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create the socket
server_socket.bind(('', port)) # listen on port 5001
server_socket.listen(5) # queue max 5 connections
client_socket, address = server_socket.accept()

print ("Your IP address is: ", socket.gethostbyname(socket.gethostname()))
print ("Server Waiting for client on port ", port)

while True:

    # test string
    #data = bytearray('DEADBEEF'.decode('hex'))
    #client_socket.sendall(data)
    
    try:
        #avoid overflow
        client_socket.sendall(stream.read(chunk, exception_on_overflow=False))
        
        #data = client_socket.recv(1024)
        #stream.write(data,chunk)
    #except IOError as e:
    #	if e[1] == pyaudio.paInputOverflowed: 
    #		print (e) 
    #		x = '\x00'*16*256*2 #value*format*chunk*nb_channels
    except Exception as e:
        print(e)
        break

stream.stop_stream()
stream.close()
socket.close()
p.terminate()
