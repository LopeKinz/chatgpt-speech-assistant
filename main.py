import speech_recognition as sr
import openai
import os
import pyttsx3

# Set up OpenAI API key and models
openai.api_key = "YOUR_API_KEY"
model_engine = "davinci"

# Initialize the recognizer and engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to recognize speech
def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source) # Reduce noise from environment
        print("Speak now...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            return text
        except:
            speak("Sorry, I did not understand that.")
            return ""

# Main loop
while True:
    # Ask for input from user
    speak("What do you want to say?")
    text = listen()

    # If the input is not empty, send it to ChatGPT
    if text:
        response = openai.Completion.create(
            engine=model_engine,
            prompt=text,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.7
        )
        response_text = response.choices[0].text.strip()

        # Speak the response
        speak(response_text)
