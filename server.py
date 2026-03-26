"""Flask server for emotion detection"""

from flask import Flask, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def detect_emotion():
    """API endpoint for emotion detection"""
    text = request.args.get('textToAnalyze')

    if text is None or text == "":
        return "Invalid input"

    result = emotion_detector(text)

    if result is None:
        return "Error processing request"

    return str(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)