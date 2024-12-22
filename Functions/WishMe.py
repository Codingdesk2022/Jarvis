from Lib.Libraries import *
from Utils.SpeechDrive import *

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("Good Morning sir")
        speak("Good Morning sir")
    elif hour>=12 and hour<18:
        print("Good Afternoon sir")   
        speak("Good Afternoon sir")   
    else:
        print("Good Evening sir")     
        speak("Good Evening sir") 