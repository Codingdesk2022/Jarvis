from Lib.Libraries import *

def speak(data):
    #voice = 'en-US-ChristopherNeural' #Jarvis
    # voice = 'en-US-AnaNeural' # Kid
    
    voice = 'en-US-ChristopherNeural' #Friday/Edith
    # voice = 'en-US-JennyNeural' #Friday/Edith
    command = f'edge-tts --voice "{voice}" --text "{data}" --write-media "data.mp3"'
    os.system(command)

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

# async def speak1(data, voice='en-US-JennyNeural'):
async def speak1(data, voice='en-US-ChristopherNeural'):
    communicate = edge_tts.Communicate(data, voice)
    await communicate.save("data.mp3")

    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("data.mp3")

    try:
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

    except Exception as e:
        print(e)
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()
