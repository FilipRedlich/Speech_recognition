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
# Load the Vosk model
model = vosk.Model("vosk-model-small-pl-0.22")

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the microphone stream
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
print("Powiedz coś...")

# Recognize text from speech using model
text = recognize_speech(model, stream)

# Print the recognized text
print(text)
# Speak out the recognized text
engine.say(text)
engine.runAndWait()

# Use recognized text as prompt in google search engine
if text.startswith("znajdź"):
    url = 'https://www.google.com/search?q=' + text[6:]
    webbrowser.open(url)

# Save recognized text to a file if it starts with "zapisz"
if text.startswith("zapisz"):
    words = text.split()
    if len(words) > 1:
        file_name = words[1] + ".txt"
        content = " ".join(words[2:])
        with open(file_name, "a") as file:
            file.write(content+"\n")
        text = f"Saved recognized speech to file: {file_name}"
        print(text)
        engine.say(text)
        engine.runAndWait()
    else:
        text = "Invalid command. Please provide a file name after keyword: 'zapisz'."
        print(text)
        engine.say(text)
        engine.runAndWait()

# Read text from a file if it starts with "odczytaj"
if text.startswith("odczytaj"):
    words = text.split()
    if len(words) > 1:
        file_name = words[1] + ".txt"
        try:
            with open(file_name, "r") as file:
                content = file.read()
            print(f"Reading text from file: {file_name}")
            engine.say(content)
            engine.runAndWait()
        except FileNotFoundError:
            text = f"File not found: {file_name}"
            print(text)
            engine.say(text)
            engine.runAndWait()
    else:
        text = "Invalid command. Please provide a file name after keyword: 'odczytaj'."
        print(text)
        engine.say(text)
        engine.runAndWait()

# Clean up
stream.stop_stream()
stream.close()
audio.terminate()
