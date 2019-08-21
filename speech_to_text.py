from ibm_watson import SpeechToTextV1
from os.path import join, dirname
import json

speech_to_text = SpeechToTextV1(
    iam_apikey='mRku2G3EtmnHGccaOihFJHvUI0VkhW07EEXij4HQtk5g',
    url='https://gateway-syd.watsonplatform.net/speech-to-text/api'
)

with open(join(dirname(__file__), './.', 'recording2.mp3'),
               'rb') as audio_file:
    speech_recognition_results = speech_to_text.recognize(
        audio=audio_file,
        content_type='audio/mp3',
    ).get_result()
print(json.dumps(speech_recognition_results, indent=2))