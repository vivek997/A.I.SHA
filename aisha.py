import webbrowser
import pyttsx3
import speech_recognition as sr
import os
import ctypes
from termcolor import colored
from tweet import api
from random_dict import que_dict
from playsound import playsound

#Owner: Vivek Rawal
#Github: vivek997

speech = sr.Recognizer()

greeting_dict = {'hello':'hello', 'hi':'hi'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}
website_dict = {'facebook': 'https://www.facebook.com', 'twitter': 'https://www.twitter.com', 'youtube': 'https://www.youtube.com'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which', 'where': 'where'}


try:
    engine = pyttsx3.init()
except ImportError:
    print('Request driver not found')
except RuntimeError:
    print('Driver fails to initialize')

voices = engine.getProperty('voices')

# for voice in voices:
#     print(voice.id)
engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

def is_valid_google_search(phrase):
    if (google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():

    voice_text = ''
    print('Listening...')
    with sr.Microphone() as source:
        audio = speech.listen(source)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        playsound('mp3/listening_problem_2.mp3')
    except sr.RequestError as e:
        print('Network error')
    return voice_text


def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.items():
        # 'Hello AISHA'
        try:
            if value == voice_note.split(' ')[0]:
                return True

            elif key == voice_note.split(' ')[1]:
                return True

        except IndexError:
            pass

    return False



if __name__ == '__main__':

    speak_text_cmd('Hello, This is Aysha as your artificial intelligence')
                                # A.I.S.H.A.
    while True:
        voice_note = read_voice_cmd().lower()
        print('cmd: {}'.format(voice_note))
        if is_valid_note(greeting_dict, voice_note):
            speak_text_cmd('Hello, How can i help you ?')
            continue
        elif voice_note in que_dict:
            speak_text_cmd(que_dict.get(voice_note))
            continue
        elif is_valid_note(open_launch_dict, voice_note):
            speak_text_cmd('sure sir.')
            if (is_valid_note(website_dict, voice_note)):
                # Launch Website
                key = voice_note.split(' ')[1]
                webbrowser.open(website_dict.get(key))
            else:
                os.system('explorer C:\\"{}"'.format(voice_note.replace('open ', '').replace('launch ', '')))
            continue
        elif 'tweet' in voice_note:
            speak_text_cmd("What's your tweet.")
            status = read_voice_cmd().lower()
            api.update_status(status)
            print('cmd: {}'.format(status))
            print(colored("successful", color='green'))
            continue
        elif is_valid_google_search(voice_note):
            print('searching...')
            playsound('mp3/search_1.mp3')
            webbrowser.open('https://www.google.co.in/search?q={}'.format(voice_note))
            continue
        elif 'lock' in voice_note:
            for value in ['pc', 'system', 'window', 'windows']:
                ctypes.windll.user32.LockWorkStation()
                speak_text_cmd('your system is locked.')
            continue
        elif 'play' in voice_note:
            webbrowser.open('https://www.saavn.com/play/featured/hindi/Weekly+Top+Songs')
            continue
        elif 'thank you' in voice_note:
            playsound('mp3/thankyou_2.mp3')
            continue
        elif 'offline' in voice_note:
            speak_text_cmd('Good Bye, happy to help you')
            exit()

