'''
Final Project
'''
import requests
import json

'''
emotion_detector
'''
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyse } }
    resp = requests.post(url, json=obj, headers=header)

    # convert resp text into dictionary
    form_resp = json.loads(resp.text)
    # form_resp is {[{'key':{}}]}

    # find dominant emotion (ie the one with the highest score)
    emotion_list = form_resp['emotionPredictions'][0].get('emotion')
    max_key = max(emotion_list,key=emotion_list.get)
    emotion_list['dominant_emotion'] = max_key
    
    return emotion_list