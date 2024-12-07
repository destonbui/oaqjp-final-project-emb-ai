import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyse } }
    
    response = requests.post(url, json = payload, headers = headers)

    response_dict  = json.loads(response.text)
    
    if response.status_code == 200:
        result = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = max(result, key = result.get)
        result['dominant_emotion'] = dominant_emotion
    elif response.status_code == 400:
        result = {'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0, 'sadness': 0, 'dominant_emotion': None}
    
    return result