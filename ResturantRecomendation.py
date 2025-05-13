import pyttsx3
import speech_recognition as sr
import datetime
import sys

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Set properties (optional, adjust as needed)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # FeMale voice, change index for male or other voices
engine.setProperty('rate', 190)  # Speech rate (speed)
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

# text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#speech to text
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listneing...")
        r.adjust_for_ambient_noise(source)
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        except sr.WaitTimeoutError:
            speak("You didn't speak. Please try again.")
            return None

    try:
        print("Recognizing..")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Please say it again.")
        return None
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return None

#wish
def wish():
    hour  = int(datetime.datetime.now().hour)

    if hour>0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good after noon")
    else:
        speak("good evening")

    speak("I am your resturant recommendation assistant")

restaurants = [
    {"name": "Spice Hub", "location": "delhi", "cuisine": "indian", "budget": 400},
    {"name": "Pizza Palace", "location": "mumbai", "cuisine": "italian", "budget": 600},
    {"name": "Dragon Express", "location": "delhi", "cuisine": "chinese", "budget": 350},
    {"name": "South Taste", "location": "bangalore", "cuisine": "south indian", "budget": 300},
    {"name": "The Urban Café", "location": "mumbai", "cuisine": "continental", "budget": 700},

    {"name": "Biryani Paradise", "location": "hyderabad", "cuisine": "mughlai", "budget": 450},
    {"name": "Mexican Magic", "location": "bangalore", "cuisine": "mexican", "budget": 500},
    {"name": "Bangkok Bites", "location": "mumbai", "cuisine": "thai", "budget": 600},
    {"name": "Punjabi Zaika", "location": "delhi", "cuisine": "punjabi", "budget": 400},
    {"name": "Khaati Peeti", "location": "amritsar", "cuisine": "punjabi", "budget": 450},

    {"name": "Thali Junction", "location": "ahmedabad", "cuisine": "gujarati", "budget": 300},
    {"name": "Rajasthani Rasoda", "location": "jaipur", "cuisine": "rajasthani", "budget": 350},
    {"name": "Mishti Mukh", "location": "kolkata", "cuisine": "bengali", "budget": 320},
    {"name": "Kashmir House", "location": "srinagar", "cuisine": "kashmiri", "budget": 500},
    {"name": "Tibetan Treats", "location": "darjeeling", "cuisine": "tibetan", "budget": 280},

    {"name": "Burger Boss", "location": "mumbai", "cuisine": "american", "budget": 450},
    {"name": "Taco Town", "location": "delhi", "cuisine": "mexican", "budget": 420},
    {"name": "Pad Thai Point", "location": "pune", "cuisine": "thai", "budget": 550},
    {"name": "Roll Nation", "location": "kolkata", "cuisine": "bengali", "budget": 280},
    {"name": "Café Kashmir", "location": "srinagar", "cuisine": "kashmiri", "budget": 460},

    {"name": "The Punjab Grill", "location": "chandigarh", "cuisine": "punjabi", "budget": 500},
    {"name": "Gujarati Ghar", "location": "surat", "cuisine": "gujarati", "budget": 320},
    {"name": "Roti Tandoor", "location": "lucknow", "cuisine": "mughlai", "budget": 410},
    {"name": "Tibet Bowl", "location": "manali", "cuisine": "tibetan", "budget": 270},
    {"name": "Spicy Thai", "location": "bangalore", "cuisine": "thai", "budget": 560},

    {"name": "Quesadilla Queen", "location": "hyderabad", "cuisine": "mexican", "budget": 480},
    {"name": "Masala Express", "location": "delhi", "cuisine": "indian", "budget": 370},
    {"name": "Waffle World", "location": "mumbai", "cuisine": "american", "budget": 400},
    {"name": "Bangkok Street", "location": "kolkata", "cuisine": "thai", "budget": 590},
    {"name": "Royal Rajasthani", "location": "udaipur", "cuisine": "rajasthani", "budget": 420},

    {"name": "Kolkata Cabin", "location": "kolkata", "cuisine": "bengali", "budget": 310},
    {"name": "Srinagar Spice", "location": "srinagar", "cuisine": "kashmiri", "budget": 530},
    {"name": "Delhi Dhaba", "location": "delhi", "cuisine": "north indian", "budget": 390},
    {"name": "Idli Café", "location": "chennai", "cuisine": "south indian", "budget": 180},
    {"name": "Chole Bhature Co.", "location": "delhi", "cuisine": "punjabi", "budget": 260},

    {"name": "American Fryhouse", "location": "pune", "cuisine": "american", "budget": 470},
    {"name": "Bombay Bento", "location": "mumbai", "cuisine": "japanese", "budget": 600},
    {"name": "Northeast Kitchen", "location": "guwahati", "cuisine": "tibetan", "budget": 300},
    {"name": "Café Mexican", "location": "goa", "cuisine": "mexican", "budget": 530},
    {"name": "Uttapam Corner", "location": "bangalore", "cuisine": "south indian", "budget": 200}
]



def get_resturant_recommendation():
    speak("Please tell me your location.")
    location = takecommand()
    if location == "none" :return

    speak("What cuisine would you like?")
    cuisine = takecommand()
    if cuisine == "none": return

    speak("What's your maximum budget?")
    budget_input = takecommand()
    try:
        budget = int(''.join(filter(str.isdigit, budget_input)))
    except:
        speak("Sorry, I couldn't understand the budget.")
        return

    results = [
        r for r in restaurants
        if r['location'].lower() == location and r['cuisine'].lower() == cuisine and r['budget'] <= budget
    ]
    
    if results:
        speak(f"I found {len(results)} restaurant(s) matching your criteria.")
        for r in results:
            speak(f"{r['name']} in {r['location'].title()}, serving {r['cuisine']} cuisine under {r['budget']} rupees.")
    else:
        speak("Sorry, I couldn't find any matching restaurants.")
    
    
if __name__ =="__main__":
    # speak("Hello Sir")
    wish()
    while True:
        speak("Would you like a restaurant recommendation?")
        ans = takecommand()
        if ans is not None and "yes" in ans:
            get_resturant_recommendation()
        elif ans is not None and "no" in ans:
            speak("Okay, have a great day!")
            break
        else:
            speak("Please say yes or no.")