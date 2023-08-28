import speech_recognition as sr
import openai
from gtts import gTTS
import playsound
import pyttsx3
import time
import os


openai.api_key = "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"

# Initialize text-to-speech engine
engine = pyttsx3.init()



# Define function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    # speak("Hello! how may I help you today?")
    with sr.Microphone() as source:
        
        print("Listening...")
        
        audio = recognizer.listen(source)

        try:
            text = recognizer.recognize_google(audio)
            print("You said:", text)
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Error connecting to Google's speech recognition service: {e}")

# Define function to speak text
def speak(text):
        engine.say(text)
        engine.runAndWait()
        return
# Define function to chat with ChatGPT


speak("Hello! how may I help you today?")
def chat(text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": text}
        ]
    )
    reply = response.choices[0].message.content.strip()
    print("ChatGPT:", reply)
    speak(reply)

# Main program loop
if __name__ == "__main__":
    while True:
        user_input = listen()
        if user_input:
            if user_input.lower() == "exit":
                print("Exiting...")
                break
            chat(user_input)
        time.sleep(1)
