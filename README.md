# IBM Watson NLP Emotion Detection

A Python application that calls an IBM Watson NLP emotion-analysis endpoint and returns scores for anger, disgust, fear, joy, and sadness, plus the dominant emotion.

## Required configuration before use
1. Open your Coursera/IBM Skills Network lab and copy its exact Watson NLP endpoint.
2. Replace `PASTE_YOUR_WATSON_NLP_ENDPOINT_HERE` in both `emotion_detection.py` and `EmotionDetection/emotion_detection.py`.
3. Verify the model ID and response schema against your lab instructions. Never publish API keys or private credentials.

## Install
```bash
python -m pip install requests flask
```

## Run unit tests
```bash
python -m unittest -v test_emotion_detection.py
```
The included tests mock the service. They do not confirm the real endpoint works.

## Run the web application
```bash
python server.py
```
Open http://127.0.0.1:5000.

## Test blank input (while the server is running)
```bash
python -c "import requests; r=requests.post('http://127.0.0.1:5000/emotionDetector', json={'text':'   '}); print(r.status_code); print(r.json())"
```
Expected behavior: HTTP 400 and a message asking for text.

## Submission evidence checklist
- [ ] Public GitHub README URL
- [ ] `emotion_detection.py` source
- [ ] Actual terminal output from import/sample test
- [ ] Formatted source and terminal output
- [ ] Public GitHub `EmotionDetection/__init__.py` URL
- [ ] Actual package import output
- [ ] `test_emotion_detection.py` and actual test results
- [ ] `server.py` and screenshot of the running interface
- [ ] Actual HTTP 400 output and blank-input screenshot
- [ ] Modified `server.py` and actual Pylint output

Capture genuine outputs/screenshots from your environment. Match filenames and requirements in the course rubric.
