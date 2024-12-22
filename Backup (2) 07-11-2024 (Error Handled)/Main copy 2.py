import subprocess
import webbrowser
import wikipedia
import random
import datetime
import os
import asyncio
import threading
from Lib.Libraries import *
from Utils.SpeechDrive import *
# from Utils.MicInput import *  # Uncomment as needed
# from Utils.KeyboardInput import *  # Uncomment as needed
# from Utils.LongSpeechDrive import *  # Uncomment as needed
from Utils.ExtractNouns import *  # extract_nouns(sentence)
from Functions.WishMe import *  # wishMe
from Functions.Weather import *  # weather
from Functions.Alarm import *  # Alarm(<time>)
from Functions.News import *  # news_Fetch
from Functions.YoutubeVideoPlay import *  # search_and_play(song_name)
from IdentityID.Identity import *  # Variables
# from ArtificialIntelligence.IntelligentSupport import *  # Uncomment as needed
from Security.master import *  # Security
# alarm_time = "04:00:00 PM"  # Example: 4:00 PM


def main():
    try:
        wishMe()
    except Exception as e:
        print(f"Error in wishMe function: {e}")
        speak("An error occurred while initializing. I'm still here to assist you.")

    while True:
        try:
            query = input("--> ").lower()
            # query = takeCommand()  # Uncomment if needed

            # Handle 'open' command
            if "open" in query:
                try:
                    N_query = query.replace("open", "")
                    NN_query = N_query.strip()
                    subprocess.Popen(f'{NN_query}')
                    speak(f"Executed {NN_query}")
                except Exception as e:
                    print(f"Error opening {NN_query}: {e}")
                    print("Opening in browser")
                    speak("Opening in browser")
                    webbrowser.open(f"https://{NN_query}.com")
                    speak(f"{NN_query} Executed")

            # Handle 'weather' command
            elif "weather" in query:
                try:
                    weather()
                except Exception as e:
                    print(f"Error in weather function: {e}")
                    speak("An error occurred while fetching the weather.")

            # Handle 'news' command
            elif "news" in query:
                try:
                    news_Fetch()
                except Exception as e:
                    print(f"Error in news fetch: {e}")
                    speak("An error occurred while fetching the news.")

            # Handle 'hello' command
            elif "hello" in query:
                speak("Hello sir")

            # Handle 'how are you' command
            elif "how are you" in query:
                speak("I am Good Sir")

            # Handle 'who are you' command
            elif "who are you" in query:
                speak(f"I’m {AI_Name} a personal virtual Assistant of Mr. Abhinav . I can streamline tasks, automate processes, and boost productivity with my intelligent and responsive support.")

            # Handle 'who is mishu' command
            elif "who is mishu" in query:
                speak("Mishu is your brother and he is very intelligent man, he is 21 years old and has brilliant skill in pencil art and sketching and by the way he is very big pig, sorry")

            # Handle 'friday' command
            elif "friday" in query:
                speak("sir")

            # Handle 'how' command (search in wikihow)
            elif "how" in query:
                try:
                    webbrowser.open(f"https://www.wikihow.com/wikiHowTo?search={query}&Search=")
                    speak("Here are the results")
                except Exception as e:
                    print(f"Error opening wikihow: {e}")
                    speak("Sorry, I couldn't open the HowTo results.")

            # Handle 'find' or 'locate' commands (search location)
            elif "find" in query or "locate" in query:
                try:
                    nouns = extract_nouns(query)
                    print("Results:", nouns)
                    webbrowser.open(f"https://www.google.com/maps/place/{nouns}")
                    speak("Here are the results")
                except Exception as e:
                    print(f"Error processing location query: {e}")
                    speak("Sorry, I couldn't process the location query.")

            # Handle 'new movies' command
            elif "new movies" in query:
                try:
                    webbrowser.open("https://in.bookmyshow.com/explore/home/national-capital-region-ncr")
                    print("New movies")
                    speak("New movies")
                except Exception as e:
                    print(f"Error opening movie website: {e}")
                    speak("Sorry, I couldn't fetch new movies.")

            # Handle 'set up environment1' command
            elif "set up environment1" in query:
                try:
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
                except Exception as e:
                    print(f"Error setting up environment 1: {e}")
                    speak("Sorry, I couldn't set up your workspace.")

            # Handle 'set up environment2' command
            elif "set up environment2" in query:
                try:
                    speak("Setting up your working Environment Boss. It may take few minutes")
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
                except Exception as e:
                    print(f"Error setting up environment 2: {e}")
                    speak("Sorry, I couldn't set up your working environment.")

            # Handle 'wikipedia' command
            elif "wikipedia" in query:
                try:
                    new_query = query.replace("wikipedia", "")
                    word = new_query
                    results = wikipedia.search(word)
                    if results:
                        suggestion = random.choice(results)
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
                            print(f"Error fetching Wikipedia summary: {e}")
                    else:
                        print("No suggestions found.")
                except Exception as e:
                    print(f"Error in Wikipedia search: {e}")
                    speak("Sorry, I couldn't fetch any results from Wikipedia.")

            # Handle 'song' or 'gaana' command
            elif "song" in query or "gaana" in query:
                try:
                    speak("searching for song")
                    song_name = query
                    speak("Playing your Music")
                    search_and_play(song_name)
                except Exception as e:
                    print(f"Error searching or playing song: {e}")
                    speak("Sorry, I couldn't find the song.")

            # Handle 'note' command
            elif "note" in query:
                try:
                    Query_without_Note = query.replace("note", "")
                    f = open("C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.6 (Step to Advance)/Notes/Notes.txt", "a")
                    writing = f"{Query_without_Note}\n"
                    f.write(writing)
                    f.close()
                    speak(f"Noted {Query_without_Note}")
                except Exception as e:
                    print(f"Error while noting: {e}")
                    speak("Sorry, I couldn't note it down.")

            # Handle 'security' command
            elif "security" in query:
                try:
                    masterSecurityKey()
                except Exception as e:
                    print(f"Error with security: {e}")
                    speak("Security operation failed.")

            # Handle 'time' command
            elif "time" in query:
                try:
                    speak(f"It's {datetime.datetime.now()}")
                except Exception as e:
                    print(f"Error getting time: {e}")
                    speak("Sorry, I couldn't fetch the time.")

            # Handle 'quit' command
            elif "quit" in query:
                speak(f"As your wish, {Greetings}")
                print("Terminated programs")
                exit()

            # Handle 'sleep' command
            elif "sleep" in query:
                try:
                    speak("I'm going to sleep sir but I am always available to assist you")
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                except Exception as e:
                    print(f"Error putting system to sleep: {e}")
                    speak("Sorry, I couldn't put the system to sleep.")

            # Handle 'lock' command
            elif "lock" in query:
                try:
                    speak("System is now going to be locked, are you sure")
                    os.system("rundll32.exe user32.dll,LockWorkStation")
                except Exception as e:
                    print(f"Error locking the system: {e}")
                    speak("Sorry, I couldn't lock the system.")

            # Handle 'speak' command
            elif "speak" in query:
                try:
                    newspeak = query.replace("speak", "")
                    speak(newspeak)
                except Exception as e:
                    print(f"Error speaking the phrase: {e}")
                    speak("Sorry, I couldn't speak that.")

            # Default command (fallback)
            else:
                try:
                    question = query
                    answer = get_answer_from_json(question)
                    print(answer)
                    asyncio.run(speakLong(answer))
                    feedback(question)
                except Exception as e:
                    print(f"Error in fallback query: {e}")
                    speak("Sorry, I couldn't understand that.")

        except Exception as e:
            print(f"An error occurred: {e}")
            speak("An unexpected error occurred, but I am still here to assist you.")


# Run the main function in a separate thread
command = threading.Thread(target=main)

if __name__ == "__main__":
    try:
        command.start()
    except Exception as e:
        print(f"Error starting the program: {e}")
        speak("There was an error starting the program.")
