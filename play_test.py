import pyaudio, sys, socket

chunk = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 48000

p = pyaudio.PyAudio()
stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, output = True, frames_per_buffer = chunk)


while True:
    try:
        #Recieve data from the server:
        stream.write(data,chunk)
    
