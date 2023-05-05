# model = vk.Model("D:/Projects/GitHub/Speech_recognition/vosk-model-small-pl-0.22")

import vosk
import json
import pyaudio

# Hide logs from vosk module
vosk.SetLogLevel(-1)

def recognize_speech(model, audio_stream):
    rec = vosk.KaldiRecognizer(model, 16000)
    while True:
        data = audio_stream.read(4000)
        if rec.AcceptWaveform(data):
            result = rec.Result()
            json_result = json.loads(result)
            text = json_result['text']
            return text

model = vosk.Model("D:/Projects/GitHub/Speech_recognition/vosk-model-small-pl-0.22")
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
print("Say something...")
text = recognize_speech(model, stream)
print(text)

stream.stop_stream()
stream.close()
audio.terminate()
