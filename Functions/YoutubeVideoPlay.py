from Lib.Libraries import *
from APIs.YoutubeAPIKey import *

def search_and_play(song_name):
    request = youtube.search().list(
        part='snippet',
        q=song_name,
        type='video',
        order='relevance',
        maxResults=1
    )
    response = request.execute()
    if response['items']:
        video_id = response['items'][0]['id']['videoId']
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        print(f"Playing: {video_url}")
        webbrowser.open(video_url)
    else:
        print("No videos found.")