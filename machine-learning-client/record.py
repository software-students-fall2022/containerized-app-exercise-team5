import pyaudio
import wave

# code inspiration taken largely from: 
# https://realpython.com/playing-and-recording-sound-python/#recording-audio
# certain necessary alterations made by Charlie Xiang for the purposes of this project


def main():

    print("Welcome to the Sentiment Analysis Recording App!\n")

    print("Ready to record? After the recording begins, it will continue to record until you hit CTRL-C.\n")

    filename = input("Type the file name that you want to save your recording under: ")

    chunk = 1024 
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    filename = filename + ".wav"

    p = pyaudio.PyAudio()

    print('Recording...')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []

    try:
        while True:
            data = stream.read(chunk)
            frames.append(data)
    except KeyboardInterrupt:
        # do nothing
        print('\nStopping recording...')

    stream.stop_stream()
    stream.close()
    p.terminate()

    print('Finished recording!')

    rec = wave.open(filename, 'wb')
    rec.setnchannels(channels)
    rec.setsampwidth(p.get_sample_size(sample_format))
    rec.setframerate(fs)
    rec.writeframes(b''.join(frames))
    rec.close()

if __name__ == "__main__":
    main()
