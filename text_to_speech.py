from ibm_watson import TextToSpeechV1

text_to_speech = TextToSpeechV1(
    iam_apikey='CCKbWIjRtnSz4aTBlPsQ9v4kApzpMyZ1hqqG86jcferM',
    url='https://stream.watsonplatform.net/text-to-speech/api'
)

lang_voice_map = {
    'en' : 'en-US_AllisonVoice', #english
    'es' : 'es-ES_EnriqueV3Voice', #spanish
    'fr' : 'fr-FR_ReneeVoice', #french
    'de' : 'de-DE_DieterVoice', #german
    'it' : 'it-IT_FrancescaV3Voice', #italian
    'ja' : 'ja-JP_EmiV3Voice' #japanese
}

def getTextAsAudio(txt, lang):
    return text_to_speech.synthesize(
            txt,
            voice = lang_voice_map[lang],
            accept='audio/mp3'        
        ).get_result().content
