from Lib.Libraries import *

def takeCommand():
    r = sr.Recognizer()

    # Adjust the recognizer sensitivity to ambient noise
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # Adjust energy threshold based on ambient noise
        print("Listening...")
        r.pause_threshold = 0.5  # Shorter pause threshold for faster recognition
        try:
            audio = r.listen(source, timeout=5)  # Timeout to prevent hanging if no speech
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"-> {query}\n")
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return "None"
        except sr.RequestError as e:
            print(f"Sorry, there was an error with the request: {e}")
            return "None"
        except Exception as e:
            print(f"An error occurred: {e}")
            return "None"
    
    return query