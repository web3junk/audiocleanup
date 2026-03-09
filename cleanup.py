#!/usr/bin/env python3
import os
os.chdir("/Users/christopherpigott/Documents")

from pydub import AudioSegment

AudioSegment.ffmpeg = "usr/local/bin/ffmpeg"

audio = AudioSegment.from_wav("dirty.wav")
print("Loaded! Lenght:", len(audio), "ms")

# ... after loading audio ...
audio = audio.high_pass_filter(80) #cuts hiss below 80z
audio = audio.low_pass_filter(8000) #cuts pops & harsh highs above 8kHz

# Target: kill 500hz hum notch it out
center_freq = 500
width = 100

audio = audio.low_pass_filter(center_freq + width / 2)
audio = audio.high_pass_filter(center_freq - width / 2)

audio.export("clean.wav", format="wav")
print("Clean file ready!")
