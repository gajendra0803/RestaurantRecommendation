from flask import Flask, request, jsonify
from voice_utils import speak, transcribe_audio
from recommend import recommend_restaurant

app = Flask(__name__)

@app.route('/')
def home():
    return "Verbly Restaurant Voice Assistant is Running!"

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    location = data.get("location")
    cuisine = data.get("cuisine")
    budget = data.get("budget")

    if not all([location, cuisine, budget]):
        return jsonify({"error": "Missing input fields."}), 400

    results = recommend_restaurant(location, cuisine, budget)
    return jsonify(results)

@app.route('/transcribe', methods=['POST'])
def transcribe():
    audio = request.files.get("audio")
    if not audio:
        return jsonify({"error": "No audio file provided."}), 400
    
    text = transcribe_audio(audio)
    return jsonify({"text": text})

@app.route('/speak', methods=['POST'])
def say():
    text = request.json.get("text")
    speak(text)
    return jsonify({"message": "Spoken successfully."})

if __name__ == '__main__':
    app.run(debug= True)
