import speech_recognition as sr
import webbrowser

# Initialize recognizer
r = sr.Recognizer()

# Use default microphone as audio source
with sr.Microphone() as source:
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    
    while True:
        try:
            # Listen for speech input
            print("Say something...")
            audio = r.listen(source, timeout=3)

            print("Recognizing...")
            # Recognize speech from audio data
            # text = r.recognize_google(audio)
            text = r.recognize_sphinx(audio)
            break
        except (sr.WaitTimeoutError, sr.UnknownValueError, sr.RequestError) as e:
            print("Error: ", e)
            continue

# Print recognized text
print(text)

if text.startswith("find me"):
    url = 'https://www.google.com/search?q=' + text[8:]
    webbrowser.open(url)
