import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pywhatkit
import pyjokes
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)

    if hour>=0 and hour<12:
        speak("Good morning sir!")
    elif 12<=hour<18:
        speak("Good afternoon sir!")
    else:
        speak("Good Evening sir!")
    speak("I'm Friday,your virtual assistant,How may I help you!")

def takecom():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold=1
        r.energy_threshold=100
        audio=r.listen(source)
    try:
        print("Recognising....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said ,{query}")
    except Exception as e:
        print("Please say again....")
        return "None"
    return query
    


    
if __name__=="__main__":
    wishme()
    while True:
         query=takecom().lower()
    
         if 'wikipedia' in query:
             speak("Searching wikipedia....")
             query=query.replace('wikipedia', "")
             result=wikipedia.summary(query,sentences=3)
             speak('According to wikipedia')
             print(result)
             speak(result)

         elif 'hi' in query:
             speak('Hello sir,nice to meet you,how may I help you')
         elif 'hello' in query:
             speak('Hello sir,nice to meet you,how may I help you')
        
         elif 'open youtube' in query:
             speak('Sure sir')
             webbrowser.open('youtube.com')

         elif 'open spotify' in query:
             speak('Sure sir')
             webbrowser.open('spotify.com')
        
         elif 'open google' in query:
             speak('Sure sir')
             webbrowser.open('google.com')
         elif 'open gfg' in query:
             speak('Sure sir')
             webbrowser.open('geeksforgeeks.org')
         elif 'open stackoverflow' in query:
             speak('Sure sir')
             webbrowser.open('stackoverflow.com')
         elif 'the time' in query:
             timestr=datetime.datetime.now().strftime("%H %M %S")  
             speak(f"Sir,The time is {timestr}")
         elif 'the day' in query:
             daystr=datetime.datetime.now().strftime('%A')
             speak(f"Its {daystr} today sir")
         elif  'open code' in query:
             speak('Sure sir')
             codepath="C:\\Users\\pc\\Downloads\\Microsoft VS Code\\Code.exe"
             os.startfile(codepath)
         elif 'stone paper scissor' in query:
             speak("Alright sir")
             while(1):
                option=['Stone','Paper','Scissor']
                user=takecom().lower()
                speak('Take your move sir...')
                compmove=[]
                temp=random.randint(1, 3)

                if temp==1:
                    compmove.append(option[0])

                elif temp==2:
                    compmove.append(option[1])

                elif temp==3:
                    compmove.append(option[2])

                if user in compmove:
                    speak("YAY!you win against me")
                else:
                    if "that's it" in user:
                        speak('Sure sir')
                        break
                    else:
                        speak(f'I thought of {compmove} TRY AGAIN')
         elif 'play song' in query:
             speak('which song would you like to play sir')
             print('Listening...')
             song=takecom().lower()
             pywhatkit.playonyt(song)

         elif 'jokes' in query:
             speak(pyjokes.get_jokes())
        
         elif 'quit' in query:
             speak('Alright,have a nice day sir')
             break