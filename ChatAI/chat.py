import openai
import speech_recognition as sr
import subprocess
from gtts import gTTS
import os
import pygame

# Atur kunci API OpenAI
openai.api_key = "API_KEY_YOUR"

def chat_with_bot(user_input):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_input,
        max_tokens=50
    )
    return response.choices[0].text.strip()

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("response.mp3")

def listen_to_user():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print("You:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            print("Sorry, there was an error with the speech recognition service.")
            return ""

def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def main():
    pygame.init()
    print("Welcome to Voice Bot!")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        
        if user_input.lower() == "listen":
            user_input = listen_to_user()
        
        bot_response = chat_with_bot(user_input)
        print("Bot:", bot_response)
        
        text_to_speech(bot_response)
        play_audio("response.mp3")

if __name__ == "__main__":
    main()
