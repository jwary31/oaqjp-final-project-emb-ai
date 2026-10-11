import requests

# Replace with the exact endpoint supplied by your Coursera/Skills Network lab.
URL = "PASTE_YOUR_WATSON_NLP_ENDPOINT_HERE"
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}


def _empty_result():
    return {"anger": None, "disgust": None, "fear": None, "joy": None,
            "sadness": None, "dominant_emotion": None}


def emotion_detector(text_to_analyze):
    if not isinstance(text_to_analyze, str) or not text_to_analyze.strip():
        return _empty_result()
    payload = {"raw_document": {"text": text_to_analyze}}
    try:
        response = requests.post(URL, json=payload, headers=HEADERS, timeout=30)
        if response.status_code == 400:
            return _empty_result()
        response.raise_for_status()
        emotions = response.json()["emotionPredictions"][0]["emotion"]
        scores = {key: emotions[key] for key in
                  ("anger", "disgust", "fear", "joy", "sadness")}
        scores["dominant_emotion"] = max(scores, key=scores.get)
        return scores
    except (requests.RequestException, ValueError, KeyError, IndexError, TypeError):
        return _empty_result()
