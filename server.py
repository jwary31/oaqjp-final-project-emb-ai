from flask import Flask, jsonify, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/emotionDetector", methods=["POST"])
def detect_emotion():
    body = request.get_json(silent=True) or {}
    text = body.get("text", "")
    if not isinstance(text, str) or not text.strip():
        return jsonify({"error": "Please enter some text."}), 400
    result = emotion_detector(text)
    if result["dominant_emotion"] is None:
        return jsonify({"error": "Emotion analysis failed. Check the input or service."}), 502
    return jsonify(result), 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
