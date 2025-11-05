#!/usr/bin/env python3.12
from gtts import gTTS
from pygame import mixer
from deep_translator import GoogleTranslator
import time
import argparse

# A dictionary of common languages and their codes
languages = {
    'English': 'en',
    'Spanish': 'es',
    'French': 'fr',
    'German': 'de',
    'Italian': 'it',
    'Portuguese': 'pt',
    'Russian': 'ru',
    'Chinese (Simplified)': 'zh-cn',
    'Japanese': 'ja',
    'Korean': 'ko',
    'Hindi': 'hi',
    'Arabic': 'ar'
}

def show_language_banner():
    print("Available Languages:")
    for language, code in languages.items():
        print(f"{language}: '{code}'")
    print("\nTo select a language, type its code (e.g., 'es' for Spanish).\n")

def translate(text, language):
    translator = GoogleTranslator(source='auto', target=language)
    return translator.translate(text)

def speak(text, language):
    tts = gTTS(text=text, lang=language)
    tts.save("speak.mp3")
    
    mixer.init()
    mixer.music.load("speak.mp3")
    mixer.music.play()

    while mixer.music.get_busy():
        time.sleep(1)

def main():
    print("=== Translator ===")
    
    # Show banner with instructions
    show_language_banner()

    parser = argparse.ArgumentParser(description='Translator')
    parser.add_argument('text', type=str, help='Text to translate')
    parser.add_argument('language', type=str, help='Language code to translate to')
    args = parser.parse_args()

    text = args.text
    language = args.language

    translation = translate(text, language)
    print(f"Translated Text: {translation}")

    # Use gTTS to speak the translated text
    speak(translation, language)

if __name__ == "__main__":
    main()
