#!/Users/pablogarcia/opt/anaconda3/envs/ibm_cloud/bin/python3.9
'''Functions to create a translator instance and translate French/English'''
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def translator_instance():
    '''Create translator instance from ibm_watson'''
    load_dotenv()
    apikey = os.environ['apikey']
    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )
    return language_translator


def english_to_french(english_text):
    '''translate english to frech with ibm translator instance'''
    load_dotenv()
    url = os.environ['url']
    language_translator=translator_instance()
    language_translator.set_service_url(url)
    if english_text!="":
        translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()
        french_text=translation['translations'][0]['translation']
        return french_text
    return "error"


def french_to_english(french_text):
    '''translate french to english with ibm translator instance'''
    load_dotenv()
    url = os.environ['url']
    language_translator=translator_instance()
    language_translator.set_service_url(url)
    #write the code here
    if french_text!="":
        translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()
        english_text=translation['translations'][0]['translation']
        return english_text
    return "error"


print(english_to_french("Hello"))