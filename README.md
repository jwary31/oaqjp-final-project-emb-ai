# Final Project: IBM Watson NLP Emotion Detection

**Repository Name:** `oaqjp-final-project-emb-ai`

A Python application that uses the IBM Watson NLP Emotion Detection service to analyze text and return scores for anger, disgust, fear, joy, and sadness, along with the dominant emotion.

## Technologies Used
- Python
- Flask
- IBM Watson NLP Emotion Detection API
- HTML, CSS, and JavaScript
- Pylint

## Required Configuration Before Use
1. Open your Coursera/IBM Skills Network lab and copy its exact Watson NLP endpoint.
2. Configure the endpoint in the appropriate emotion detection Python file.
3. Verify the model ID and response format against the lab instructions.
4. Never publish API keys or private credentials.

## Install
```bash
python3 -m pip install requests flask
```

## Run Unit Tests
```bash
python3 -m unittest -v test_emotion_detection.py
```

## Run the Web Application
```bash
python3 server.py
```

Open the application through your lab environment's preview on port 5000.

## Error Handling
The application checks for blank input and displays an error message when the input is invalid.

## Project Files
- `EmotionDetection/emotion_detection.py` — analyzes text and returns emotion scores.
- `EmotionDetection/__init__.py` — exposes the emotion detection function.
- `server.py` — runs the Flask web application.
- `test_emotion_detection.py` — contains unit tests.
- `static/` and `templates/` — contain the web interface files.

## Static Code Analysis
Pylint is used to check the Python code for coding errors and style issues.
