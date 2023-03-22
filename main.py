import speech_recognition as sr


speech_engine = sr.Recognizer()



def from_microphone():
    with sr.Microphone() as micro:
        print("Recording...")
        audio = speech_engine.record(micro, duration=5)
        print("Recognition...")
        text = speech_engine.recognize_google(audio, language="de-DE")
        return text

print(from_microphone())
