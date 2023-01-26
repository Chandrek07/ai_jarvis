import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("GOOD MORNING CHANDREK")

    elif 12 <= hour < 18:
        speak("GOOD AFTERNOON CHANDREK")

    else:
        speak("GOOD EVENING CHANDREK")

    speak("HELLO HOW ARE YOU, What help can i do for you")


def takeCommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Using google for voice recognition.
        print(f"User said: {query}\n")  # User query will be printed.
    except Exception as e:
        print("Say that again please...")  # Say that again will be printed in case of improper voice
        return "None"  # None string will be returned
    return query


def sendEmail(content, to):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('chandreks123@gmail.com', 'your-Kuchbhini@6789')
    server.sendmail('chandreks123@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("https://www.google.co.in/")

        elif 'best footballer in the world' in query:
            speak('CHRISTIANO RONALDO  The Real GOAT')

        elif 'play music' in query:
            music_dir = 'E:\\music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'email to chandu' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "chandrekd123@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend chandrek bro . I am not able to send this email")
        elif 'open my photos' in query:
            photoPath = "E:\\my photos"
            photos = os.listdir(photoPath)
            os.startfile(os.path.join(photoPath, photos[0]))

        elif 'ok bye' in query:
            exit()

        elif 'open my insta' in query:
            webbrowser.open("https://www.instagram.com/dark_s0ul_07/")

        elif 'open my whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
