import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty('rate', 190)
engine.setProperty('volume', 1)

def speak(text):
    print(f"SPEAK: {text}")
    engine.say(text)
    engine.runAndWait()

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio, language='en-IN')
    except Exception as e:
        return str(e)
