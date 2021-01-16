import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import random
import sys


machine = pyttsx3.init('sapi5')
voices = machine.getProperty('voices')
machine.setProperty('voice', voices[1].id)

def speak(audio):
    machine.say(audio)
    machine.runAndWait()

def soul():
    r = sr.Recognizer()
    with sr.Microphone() as lope:
        print("Say Sentence to Search On Google Sir....")
        speak("Say Sentence to Search On Google Sir....")
        r.adjust_for_ambient_noise(lope, duration=5)
        audio = r.listen(lope)
    try:
        print("Searching On Google Sir.....")    
        speak("Searching On Google Sir.....")
        motor = r.recognize_google(audio, language="en-in")
        print("You had Said Sir :- " + motor)
        webbrowser.open("https://google.com/?#q=" + motor)

    except Exception as p:
        print("Say That Again Sir....")        
        speak("Say That Again Sir....") 
        return "None"
    return motor  

def morningwishing():
    pot = int(datetime.datetime.now().hour)
    if pot >= 0 and pot <12:
        speak("Good Morning Sir, JARVIS is Online")
    elif pot >= 12 and pot <18:
        speak("Good AfterNoon Sir, JARVIS is Online")
    else:
        speak("Good Evening Sir, JARVIS is Online")

def takeVoice():
    r = sr.Recognizer()
    with sr.Microphone() as maininput:
        print("Listening Your Command Sir.....")
        speak("Listening Your Command Sir.....")
        r.adjust_for_ambient_noise(maininput, duration=2)
        audio = r.listen(maininput)
    try:
        print("Recognizing Your Command Sir.....")    
        speak("Recognizing Your Command Sir.....")
        null = r.recognize_google(audio, language="en-in")
        print("You had Said Sir :- " + null)

    except Exception as p:
        print("Say That Again Sir....")        
        speak("Say That Again Sir....") 
        return "None"
    return null

if __name__ == '__main__':
    morningwishing()
    while True:
         null = takeVoice().lower()

         if "open google" in null:
            print("Opening Google For You Sir...")
            speak("Opening Google For You Sir...")
            webbrowser.open("https://google.com/")
         elif "search google" in null:
             print("Preparing Search Command For You, Wait a Second Sir..")   
             speak("Preparing Search Command For You, Wait a Second Sir..")
             soul()
         elif "youtube" in null:
             print("Opening Youtube For You Sir...")       
             speak("Opening Youtube For You Sir...")   
             webbrowser.open("https://youtube.com/")
         elif "chrome" in null:
             print("Opening Chrome For You Sir....")        
             speak("Opening Chrome For You Sir....")   
             os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
         elif "play song" in null:
             print("Playing Song For You Sir...")
             speak("Playing Song For You Sir...")    
             pop = ["E:\\Songs\\_Mushkil_Kushaan__Shahid_Mallya_Latest_Video_Song___Page_16___Kiran_Kumar,Aseem_.mp3", "E:\\Songs\\02 Darkhaast - Shivaay (Arijit Singh) 190Kbps.mp3"]

             olo = random.choice(pop)
             os.startfile(olo)

         elif "stop" in null:
             sys.exit()
            
            
                   

