import pyaudio
import wave


def main():

    print("Welcome to the Sentiment Analysis Recording App!\n")

    # p = pyaudio.PyAudio()
    # info = p.get_host_api_info_by_index(0)
    # numdevices = info.get('deviceCount')

    # print("Here are your input devices:\n")

    # for i in range(0, numdevices):
    #     if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
    #         print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'), "\n")
    #         print("Input Device id ", i, " - ", p.get_device_info_by_host_api_device_index(0, i).get('name'), "\n")


    print("Ready to record? After the recording begins, it will continue to record until you hit CTRL-C.\n")

    filename = input("Type the file name that you want to save your recording under: ")

    chunk = 1024 
    sample_format = pyaudio.paInt16
    # channels = 2
    channels = 1
    fs = 44100
    # seconds = 3
    filename = filename + ".wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording...')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    # for i in range(0, int(fs / chunk * seconds)):
    #     data = stream.read(chunk)
    #     frames.append(data)

    try:
        while True:
            data = stream.read(chunk)
            frames.append(data)
    except KeyboardInterrupt:
        # do nothing
        print('\nStopping recording...')

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording!')

    # Save the recorded data as a WAV file
    rec = wave.open(filename, 'wb')
    rec.setnchannels(channels)
    rec.setsampwidth(p.get_sample_size(sample_format))
    rec.setframerate(fs)
    rec.writeframes(b''.join(frames))
    rec.close()

if __name__ == "__main__":
    main()
