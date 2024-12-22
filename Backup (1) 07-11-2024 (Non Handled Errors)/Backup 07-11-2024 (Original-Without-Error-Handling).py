from Lib.Libraries import *

from Utils.SpeechDrive import * # speak
from Utils.MicInput import * # takeCommand
from Utils.KeyboardInput import * # GetQuery
from Utils.LongSpeechDrive import * # speakLong
from Utils.ExtractNouns import * # extract_nouns(sentence)

from Functions.WishMe import * # wishMe
from Functions.Weather import * # weather
from Functions.Alarm import * # Alarm(<time>)
from Functions.News import * # news_Fetch
from Functions.YoutubeVideoPlay import * # search_and_play(song_name)

from IdentityID.Identity import * # Variables

# from ArtificialIntelligence.IntelligentSupport import *

from Security.master import *

# alarm_time = "04:00:00 PM"  # Example: 4:00 PM
def main():
    wishMe()
    while True:
        query = input("--> ").lower()
        # query = takeCommand()
        if "open" in query:
            N_query = query.replace("open", "")
            NN_query = N_query.strip()
            try:
                subprocess.Popen(f'{NN_query}')
                speak(f"Executed {NN_query}")
            except Exception as e:
                print(e)
                print("Opening in browser")
                speak("Opening in browser")
                webbrowser.open(f"https://{NN_query}.com")
                speak(f"{NN_query} Executed")
        
        elif "weather" in query:
            weather()
        
        elif "news" in query:
            news_Fetch()
        
        elif "hello" in query:
            speak("Hello sir")
        elif "how are you" in query:
            speak("I am Good Sir")
        elif "who are you" in query:
            speak(f"I’m {AI_Name} a personal virtual Assistant of Mr. Abhinav . I can streamline tasks, automate processes, and boost productivity with my intelligent and responsive support.")
        elif "who is mishu" in query:
            speak("Mishu is your brother and he is very intelligent man, he is 21 years old and have a brilliant skill in pencil art and sketching and by the way he is very big pig, sorry")
        elif "friday" in query:
            speak("sir")

        elif "how" in query:
            webbrowser.open(f"https://www.wikihow.com/wikiHowTo?search={query}&Search=")
            speak("Here are the results")
        
        elif "find" in query:
            nouns = extract_nouns(query)
            print("Results:", nouns)
            webbrowser.open(f"https://www.google.com/maps/place/{nouns}")
            speak("Here are the results")

        elif "locate" in query:
            nouns = extract_nouns(query)
            print("Results:", nouns)
            webbrowser.open(f"https://www.google.com/maps/place/{nouns}")
            speak("Here are the results")
            
        elif "new movies" in query:
            webbrowser.open("https://in.bookmyshow.com/explore/home/national-capital-region-ncr")
            print("New movies")
            speak("New movies")

        elif "set up environment1" in query:
            speak("Setting up your workspace 1 Environment. It may take few minutes")
            webbrowser.open("https://freelancer.com")
            webbrowser.open("https://upwork.com")
            webbrowser.open("https://gmail.com")
            webbrowser.open("https://web.whatsapp.com")
            chrome_path = "C:/Users/Infort/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe"
            url1 = "http://instagram.com"
            subprocess.run([chrome_path, "--incognito", url1])
            url2 = "http://drive.google.com"
            subprocess.run([chrome_path, "--incognito", url2])
            url3 = "http://gmail.com"
            subprocess.run([chrome_path, "--incognito", url3])
            speak("Environment setup complete")
        elif "set up environment2" in query:
            speak(f"Setting up your working Environment Boss. It may take few minutes")
            webbrowser.open("https://chatgpt.com")
            webbrowser.open("https://stackoverflow.com")
            webbrowser.open("https://datasetsearch.research.google.com")
            webbrowser.open("https://web.whatsapp.com")
            chrome_path = "C:/Users/Infort/AppData/Local/BraveSoftware/Brave-Browser/Application/brave.exe"
            url1 = "http://instagram.com"
            subprocess.run([chrome_path, "--incognito", url1])
            url2 = "http://youtube.com"
            subprocess.run([chrome_path, "--incognito", url2])
            url3 = "http://gmail.com"
            subprocess.run([chrome_path, "--incognito", url3])
            speak("Environment setup complete")
        
        elif "wikipedia" in query:
            new_query = query.replace("wikipedia", "")
            word = new_query
            results = wikipedia.search(word)
            if results:
                # If there are multiple suggestions, pick one at random
                suggestion = random.choice(results)
                # print(f"Chosen suggestion: {suggestion}")
                speak(f"{suggestion}")
            try:
                f = open("data.txt", "w")
                f.write(wikipedia.summary(suggestion))
                f.close()
                with open("data.txt", "r") as file:
                    content = file.read().replace("\n", " ").strip()
                    print(content)
                    asyncio.run(speak1(content))
            except wikipedia.exceptions.DisambiguationError as e:
                print(f"DisambiguationError: {e.options}")
            except wikipedia.exceptions.PageError:
                print("PageError: Page not found.")
            except Exception as e:
                print(f"An error occurred: {e}")
            else:
                print("No suggestions found.")
        
        elif "song" in query or "gaana" in query:
            speak("searching for song")
            song_name = query
            speak("Playing your Music")
            search_and_play(song_name)

        elif "note" in query:
            Query_without_Note = query.replace("note", "")
            f = open("C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.6 (Step to Advance)/Notes/Notes.txt", "a")
            writing = f"{Query_without_Note}\n"
            f.write(writing)
            f.close()
            speak(f"Noted {Query_without_Note}")

        elif "security" in query:
            masterSecurityKey()
            # print("Security Test Passes")

        elif "time" in query:
            speak(f"It's {datetime.datetime.now()}")
        elif "quit" in query:
            speak(f"As your wish, {Greetings}")
            print("Terminated programs")
            exit()
        elif "sleep" in query:
            speak("I'm going to sleep sir but i am always available to assist you")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        elif "lock" in query:
            speak("System is now going to be locked, are you sure")
            os.system("rundll32.exe user32.dll,LockWorkStation")
        elif "speak" in query:
            newspeak = query.replace("speak", "")
            speak(newspeak)
        
        else:
            # print("I don't know about it, Taking Help of Intelligent Support")
            question = query
            answer = get_answer_from_json(question)
            # print("Answer:", answer)
            print(answer)
            asyncio.run(speakLong(answer))
            feedback(question)


command = threading.Thread(target=main)
if __name__ == "__main__":
    main()