import pyttsx3
import speech_recognition as sr
import datetime


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning madam!")
    elif hour >= 12 and hour < 14:
        speak("Good Afternoon madam!")
    else:
        speak("Good Evening madam!")

    speak("I am your personal assistant ....How may I help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognising....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")

    except Exception as e:
        # print(e)
        print("Say again please...")
        return "None"
    return query


if __name__ == "__main__":

    wishMe()

    while True:
        query = takeCommand().islower()
        





















































































































































        