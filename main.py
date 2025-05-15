from google.cloud import texttospeech
from flask import Flask, request, jsonify
import os

app = Flask(__name__)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "your-service-account.json"

client = texttospeech.TextToSpeechClient()

@app.route("/speak", methods=["POST"])
def synthesize_speech():
    data = request.json
    input_text = texttospeech.SynthesisInput(text=data["text"])

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US", name="en-US-Wavenet-D"
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )

    response = client.synthesize_speech(
        input=input_text, voice=voice, audio_config=audio_config
    )

    with open("output.mp3", "wb") as out:
        out.write(response.audio_content)

    return jsonify({"message": "Audio created", "file": "output.mp3"})

if __name__ == "__main__":
    app.run(debug=True)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

