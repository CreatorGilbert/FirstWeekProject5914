import json
from os.path import join, dirname
from ibm_watson import TextToSpeechV1

service = TextToSpeechV1(
    url='https://stream.watsonplatform.net/text-to-speech/api',
    iam_apikey='KWP30j6kirmcGn95oJoTIR-HHQth-UIu-OndIRqN70UI'
                        )

with open(join(dirname(__file__), './sample.wav'),
          'wb') as audio_file:
    response = service.synthesize(
        'sample test to get the text to speech', accept='audio/wav',
        voice="en-US_AllisonVoice").get_result()
    audio_file.write(response.content)
