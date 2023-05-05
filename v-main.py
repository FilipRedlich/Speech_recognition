# model = vk.Model("D:/Projects/GitHub/Speech_recognition/vosk-model-small-pl-0.22")

import vosk
import sys
import os
import wave
import json
import pyaudio

def recognize_speech(model, audio_stream, rate):
    rec = vosk.KaldiRecognizer(model, 16000)
    while True:
        data = audio_stream.read(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            json_result = json.loads(result)
            text = json_result['text']
            return text
    result = rec.FinalResult()
    json_result = json.loads(result)
    text = json_result['text']
    return text

model = vosk.Model("D:/Projects/GitHub/Speech_recognition/vosk-model-small-pl-0.22")
audio = pyaudio.PyAudio()
rate = 16000
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=rate, input=True, frames_per_buffer=8000)
print("TALK NOW")
text = recognize_speech(model, stream, rate)
print(text)

stream.stop_stream()
stream.close()
audio.terminate()
