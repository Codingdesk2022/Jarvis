from Lib.Libraries import *
from Utils.SpeechDrive import *
from APIs.newsAPIKey import *

def news_Fetch():
    # API_KEY = "c8ac4e318754440aa5450e5d4c4bb025"
    Query = "Apple"
    Date_Range = "2024-08-22"
    sortby = "popularity"
    
    # Fetch news from API
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey=c8ac4e318754440aa5450e5d4c4bb025")
    
    # Print the response status to check if the API call is successful
    print(f"Status Code: {response.status_code}")  # Should be 200 if successful
    if response.status_code != 200:
        print("Failed to fetch news. Exiting...")
        return

    # Load JSON data
    data = response.json()

    # Print the data for debugging
    print(data)  # This helps us check if we are getting articles in the response
    
    # Check if response contains articles
    if 'articles' not in data or len(data['articles']) == 0:
        print("No articles found.")
        print("Might be Because we are out of requests of News. We can try to wait for 24 hours to reset")
        return
    
    articles = data['articles']
    extracted_info = []

    for article in articles:
        info = {
            'source_name': article['source']['name'],
            'author': article['author'],
            'title': article['title'],
            'url': article['url']
        }
        extracted_info.append(info)

    # Iterate through extracted articles
    for item in extracted_info:
        print(f"Source Name: {item['source_name']}")
        speak(f"Source, {item['source_name']}")
        
        print(f"Author: {item['author']}")
        speak(f"Author, {item['author']}")
        
        print(f"Title: {item['title']}")
        speak(f"{item['title']}")
        
        print(f"URL: {item['url']}")
        print("Url for detailed article")
        print()

        # Get user input for navigation
        next_action = input("Press Enter to move on, or type 'e'/'q' to exit: ")

        # Handle navigation based on user input
        if next_action == "":
            continue  # Continue to the next article
        elif next_action.lower() in ['e', 'q']:
            break  # Exit the loop
        else:
            print("Invalid input. Moving to the next article.")
            speak("No more news for today, sir.")
