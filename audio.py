# -*- utf-8 -*-
# @Time:  2023/3/9 19:16
# @Autor: Andy Ye
# @File:  audio.py
# @IDE: PyCharm

import pyaudio
import wave
import threading as td


def record(time=3, file_path='record.wav'):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 1
    sr = 16000  # samp
    seconds = time
    # filename = "output.wav"

    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=sr,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(sr / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(sr)
    wf.writeframes(b''.join(frames))
    wf.close()


class Recorder(td.Thread):
    def __init__(self, file_path='record.wav', chunk=1024, channel=1, sampling_rate=16000, sample_format=pyaudio.paInt16,
                 time=None, daemon=True):
        super().__init__(daemon=daemon)
        self.file_path = file_path
        self.chunk = chunk
        self.time = time
        self.channel = channel
        self.p = pyaudio.PyAudio()
        self.sr = sampling_rate
        self.sample_format = sample_format
        self.enabled = True

    def run(self):
        stream = self.p.open(format=self.sample_format,
                        channels=self.channel,
                        rate=self.sr,
                        frames_per_buffer=self.chunk,
                        input=True)

        frames = []  # Initialize array to store frames

        print('Recording')
        while self.enabled:
            data = stream.read(self.chunk)
            frames.append(data)
            # Stop and close the stream
        stream.stop_stream()
        stream.close()
        # Terminate the PortAudio interface
        self.p.terminate()
        print('Finished recording')
        wf = wave.open(self.file_path, 'wb')
        wf.setnchannels(self.channel)
        wf.setsampwidth(self.p.get_sample_size(self.sample_format))
        wf.setframerate(self.sr)
        wf.writeframes(b''.join(frames))
        wf.close()

    def stop(self):
        self.enabled = False


if __name__ == '__main__':
    # record()
    import time
    recorder = Recorder(file_path='test_record.wav', chunk=1024)
    recorder.start()
    time.sleep(3)
    recorder.stop()
    time.sleep(2)
