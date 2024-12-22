from Lib.Libraries import *
from Utils.SpeechDrive import *

def Alarm(alarm_time):
    while True:
        current_time = datetime.datetime.now().strftime("%I:%M:%S %p")
        if current_time == alarm_time:
            print("The specified time has been reached!")
            speak(f"The specified time has been reached! Sir")
            break
        time.sleep(1)  # Sleep for 1 second to avoid busy waiting