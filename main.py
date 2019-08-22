from speech_to_text import speechToText


def mostLikelyTranscript(response):
    #assuming they are already sorted TODO sort em
    return response['results'][0]['alternatives'][0]['transcript']

def getEnglishPhrase(audiofile):
    s_t_t_response = speechToText(audiofile)
    return mostLikelyTranscript(s_t_t_response)

def translatePhrase(phrase, lang):
    return 'a translated phrase'
     
def outPutAudio(audio):
    print('outputting a file')

def getTextAsAudio(txt):
    return 'an audio file'


def speakOtherLanguage(lang, audiofile):
    eng_txt = getEnglishPhrase(audiofile)
    trans_txt = translatePhrase(eng_txt, lang)
    outPutAudio(getTextAsAudio(trans_txt))



#example
speakOtherLanguage('Spanish', 'recording2.mp3')



