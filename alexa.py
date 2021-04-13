import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

# SAPI is an API developed by Microsoft to allow the use of speech recognition and
# speech synthesis within Windows applications
engine = pyttsx3.init('sapi5')

# voices can be male and female 0 for male and 1 for female
voices = engine.getProperty('voices')

# print(voices[1].id) or print(voices[0].id) or just print(voices)
engine.setProperty('voice', voices[0].id)

# whatever audio argument will be given to our ai it will speak it out
def speak(audio): 
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am amaan's personal assistant. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer() #recognizer is a class....press ctrl and then click on Recognizer
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 #seconds of non speaking audio before a phrase is considered complete..we have rechanged its value
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n") # or print("User said:", query)

    except Exception as e:
        # print(e)  <-- it has been commented bcoz we dont want to print the error as it will would look dirty  
        print("Say that again please...")  
        return "None"
        
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1: <-- this only if u want ur loop t run only one time
        query = takeCommand().lower() #converted in small letters since in line 68 "wikipedia" also in small

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "") #now query is empty
            results = wikipedia.summary(query, sentences=2) #it will read 2 sentences
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            music_dir = 'xyz' # music_dir stands for music directory in our pc
            songs = os.listdir(music_dir) # it will make list of songs in music_dir directory
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0])) # os.startfile will start file whose path is os.path.join(music_dir, songs[0])

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strftime}")

        elif 'open code' in query:
            codePath = "xyz.py"
            os.startfile(codePath) 

        elif "quit" in query:
            exit()

          



