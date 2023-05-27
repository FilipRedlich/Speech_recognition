import vosk
import json
import pyaudio
import pyttsx3
import webbrowser

# Hide logs from vosk module
vosk.SetLogLevel(-1)

# Initialize pyttsx3
engine = pyttsx3.init()

# Set the desired language
engine.setProperty('voice', 'pl')

def recognize_speech(model, audio_stream):
    rec = vosk.KaldiRecognizer(model, 16000)
    while True:
        data = audio_stream.read(4000)
        if rec.AcceptWaveform(data):
            result = rec.Result()
            json_result = json.loads(result)
            text = json_result['text']
            return text

# Models url = https://alphacephei.com/vosk/models
model = vosk.Model("D:/Projects/GitHub/Speech_recognition/vosk-model-small-pl-0.22")
audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
print("Powiedz coś...")
text = recognize_speech(model, stream)
print(text)
engine.say(text)  # Speak out the final transcription
engine.runAndWait()

if text.startswith("znajdź"):
    url = 'https://www.google.com/search?q=' + text[8:]
    webbrowser.open(url)

stream.stop_stream()
stream.close()
audio.terminate()
