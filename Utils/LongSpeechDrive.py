from Lib.Libraries import *

async def speaklong(data, voice='en-US-ChristopherNeural'):
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
    
async def speakLong(text):
    await speaklong(text, "en-US-JennyNeural")