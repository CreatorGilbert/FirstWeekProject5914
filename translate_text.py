import json
from ibm_watson import LanguageTranslatorV3

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    iam_apikey='8WxtaSa4SHZ6RhXWfrn4l8vrTo0yzPk_1r3cnCwZYg_V',
    url='https://gateway.watsonplatform.net/language-translator/api')

def translateText(txt, to_lang, from_lang ='en'):
    return language_translator.translate(
        text=txt,
        source=from_lang,
        target=to_lang).get_result()
