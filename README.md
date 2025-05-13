# RestaurantRecommendation
A repository for verblyAI
This project is a basic voice assistant that provides restaurant recommendations based on location, cuisine, and budget, using voice-based interaction. It is built as part of Preliminary Test 2 of the Verbly AI project. 
 Features Implemented
✅ Voice Input using speech_recognition

✅ Voice Output using pyttsx3

✅ Basic restaurant recommendation system from a predefined dataset

✅ Handles user queries for:

Location

Cuisine preference

Budget (with voice parsing of numbers)

✅ Outputs results as spoken responses

✅ Interactive loop for repeated queries

✅ Time-based greetings

🧠 Tech Stack Used
Python

pyttsx3 for Text-to-Speech

speech_recognition for Speech-to-Text

Standard Python libraries: datetime, sys

Project Structure
main.py             # Core logic for voice assistant
├── README.md     

How to Run
Install dependencies:

bash
Copy
Edit
pip install pyttsx3 SpeechRecognition pyaudio
(Note: pyaudio may require additional setup depending on your OS.)

Run the assistant:

bash
Copy
Edit
python main.py
Interact via your microphone. The assistant will:

Greet you based on the time of day

Ask if you want restaurant recommendations

Take your location, cuisine preference, and budget

Speak out matching restaurant suggestions

 Limitations
Only supports English voice input for now.

Restaurant data is hardcoded and not fetched from an API or external source.

Does not handle follow-up questions like "cheaper options near Bandra."

No LLM or API integration yet.



Note: Can integrate LLM because of its cost of Key I tried to Integrate LLM but it always said quota out of limit
