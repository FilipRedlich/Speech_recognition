import speech_recognition as sr

# Initialize recognizer
r = sr.Recognizer()

# Use default microphone as audio source
with sr.Microphone() as source:
    # Adjust for ambient noise
    r.adjust_for_ambient_noise(source)
    
    while True:
        # Listen for speech input
        print("Say something...")
        try:
            audio = r.listen(source, timeout=1)
            break
        except sr.WaitTimeoutError:
            print("Timed out waiting for speech input. Please try again.")
            continue

print("Recognizing")
# Recognize speech from audio data
text = r.recognize_google(audio)

# Print recognized text
print(text)
