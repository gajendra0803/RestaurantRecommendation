import requests
import pyttsx3
import speech_recognition as sr
import datetime
import sys
import time
import json

# ElevenLabs API key
api_key = 'sk_485e750cc0868cf42ba355001898661b1ff88cb558ea0f8d'

# Function to convert text to speech using ElevenLabs
def speak(audio, lang='en'):
    url = "https://api.elevenlabs.io/v1/text-to-speech/stream"  # Correct endpoint
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "text": audio,
        "voice": "en_us_male" if lang == 'en' else "hi_in_female",  # Set voice based on language
        "model_id": "elevenlabs/expressive",  # Check if your plan allows this model
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        audio_data = response.content
        with open("output_audio.wav", "wb") as audio_file:
            audio_file.write(audio_data)
        # Play the audio file
        from playsound import playsound
        playsound("output_audio.wav")
        print(audio)
    else:
        print(f"Error: {response.status_code} - {response.text}")
        speak("Sorry, I couldn't process the request. Please try again.", lang)

# Speech to text function
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("You didn't speak. Please try again.")
            return None

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please say it again.")
        return None
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return None

# Greeting function
def wish():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour <= 12:
        speak("Good morning", lang='en')
    elif hour > 12 and hour < 18:
        speak("Good afternoon", lang='en')
    else:
        speak("Good evening", lang='en')
    speak("I am your restaurant recommendation assistant.", lang='en')

# Restaurant recommendation function
restaurants = [
    {"name": "Spice Hub", "location": "delhi", "cuisine": "indian", "budget": 400},
    {"name": "Pizza Palace", "location": "mumbai", "cuisine": "italian", "budget": 600},
    # Add more restaurants...
]

def get_restaurant_recommendation():
    speak("Please tell me your location.", lang='en')
    location = takecommand()
    if location == "none":
        return

    speak("What cuisine would you like?", lang='en')
    cuisine = takecommand()
    if cuisine == "none":
        return

    speak("What's your maximum budget?", lang='en')
    budget_input = takecommand()
    try:
        budget = int(''.join(filter(str.isdigit, budget_input)))
    except:
        speak("Sorry, I couldn't understand the budget.", lang='en')
        return

    results = [
        r for r in restaurants
        if r['location'].lower() == location and r['cuisine'].lower() == cuisine and r['budget'] <= budget
    ]
    
    if results:
        speak(f"I found {len(results)} restaurant(s) matching your criteria.", lang='en')
        for r in results:
            speak(f"{r['name']} in {r['location'].title()}, serving {r['cuisine']} cuisine under {r['budget']} rupees.", lang='en')
    else:
        speak("Sorry, I couldn't find any matching restaurants.", lang='en')

# Main program loop
if __name__ == "__main__":
    wish()
    while True:
        speak("Would you like a restaurant recommendation?", lang='en')
        ans = takecommand()
        if ans is not None and "yes" in ans:
            get_restaurant_recommendation()
        elif ans is not None and "no" in ans:
            speak("Okay, have a great day!", lang='en')
            break
        else:
            speak("Please say yes or no.", lang='en')

        # Code for switching to Hindi
        speak("Chahen to aap Hindi mein bhi baat kar sakte hain.", lang='hi')
        ans_hindi = takecommand()
        if ans_hindi is not None and "yes" in ans_hindi:
            speak("Aap hindi mein baat kar rahe hain", lang='hi')
            # You can add additional logic here for responding in Hindi.
