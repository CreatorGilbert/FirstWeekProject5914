from speech_to_text import speechToText
from text_to_speech import getTextAsAudio
from translate_text import translateText

from os.path import join

debug = True

def mostLikelyTranscript(response):
    #assuming they are already sorted descending TODO select highest confidence
    return response['results'][0]['alternatives'][0]['transcript']

def getEnglishPhrase(audiofile):
    s_t_t_response = speechToText(audiofile)
    return mostLikelyTranscript(s_t_t_response)

     
def outPutAudio(audio, filename):
    with open(join('output', filename), 'wb') as audio_file:
        audio_file.write(audio)

def firstTranslation(translations):
    return translations['translations'][0]['translation']

def speakOtherLanguage(lang, audiofile):
    eng_txt = getEnglishPhrase(audiofile)
    if debug:
        print('stt result: ' + eng_txt)
    trans_txt = firstTranslation(translateText(eng_txt, lang))
    if debug:
        print('translated to ' + lang + ': ' + trans_txt)
    outPutAudio(getTextAsAudio(trans_txt, lang),eng_txt[:10]+ '-' + lang + '.mp3')






