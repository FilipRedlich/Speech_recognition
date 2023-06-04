**************************************************
Speech Recognition Program Documentation
**************************************************

Introduction:
--------------
This program uses the Vosk speech recognition library along with PyAudio and pyttsx3 to perform real-time speech recognition, text-to-speech conversion, and execute certain actions based on recognized speech. The program allows users to interact with the system by speaking commands and performing actions accordingly.

Dependencies:
--------------
- vosk: Vosk is an open-source speech recognition library that provides offline speech recognition capabilities. It is used for recognizing speech input in real-time.
- pyaudio: PyAudio is a Python library that provides bindings for the PortAudio audio I/O library. It is used for recording audio from the microphone and playing back audio.
- pyttsx3: pyttsx3 is a Python library that provides a cross-platform text-to-speech interface. It is used for converting recognized text to spoken words.
- webbrowser: webbrowser is a built-in Python module that provides a high-level interface to open web browsers. It is used to perform web searches based on recognized speech.
- requests: requests is a Python library that provides ability to send HTTP requests. It is used for sending data from python to the web server.

Usage:
--------------
1. Ensure that the required dependencies are installed.
2. Download the Vosk model for the desired language and specify the model path in the code.
3. Run the program.
4. Speak commands or prompt the program with speech input.

Features:
--------------
1. Real-time Speech Recognition: The program uses the Vosk library to perform real-time speech recognition from the microphone input.
2. Text-to-Speech Conversion: The program uses pyttsx3 to convert recognized text to spoken words.
3. Command Execution: Define specific commands and perform corresponding actions based on recognized speech.
4. Google Search: Perform web searches based on recognized speech starting with the "znajdź" keyword.
5. Speech-to-File Saving: Save recognized speech to a file if it starts with the "zapisz" keyword.
6. File Reading: Read text from a file if it starts with the "odczytaj" keyword.
7. Multilingual Support: Set the desired language for speech recognition and text-to-speech conversion.

Additional Functions:
--------------
Sending Recognized Text to a Web Server: The program can send the recognized text to a web server hosted on localhost using the HTTP protocol.
Displaying Recognized Text in a Three-Column Table: The program provides a simple web interface that displays the received recognized text in a three-column table layout.

Important Notes:
--------------
- Make sure to replace the Vosk model path with the correct model path on your system.
- Ensure that the necessary permissions are granted to access the microphone and write files to the system.

