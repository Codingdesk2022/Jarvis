import json
from Security import ACCESS_GRANTED
from Security import data
import shutil

from Lib.Libraries import *
# from Utils.SpeechDrive import *

def printf(text):
    # Get the terminal size
    terminal_width = shutil.get_terminal_size().columns
    
    # Split text into lines in case it's multi-line
    lines = text.split('\n')
    
    for line in lines:
        # Calculate the padding on the left to center the text
        padding = (terminal_width - len(line)) // 2
        centered_line = ' ' * padding + line
        print(centered_line)

# Function to write content to a file
def write_to_file(content, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)  # Write content to file
        print(f"Content written to {file_path} successfully.")
    except Exception as e:
        print(f"Error writing to file: {e}")

# Function to read content from a file and store it in a variable
def read_from_file(file_path, variable):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            variable[0] = file.read()  # Store file content in the first element of the list
        print(f"Content read from {file_path} successfully.")
    except Exception as e:
        print(f"Error reading from file: {e}")


def masterSecurityKey():
    # Open the JSON file and load its content
    for i in range(0, 1, 1):
        with open('C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.9 (Matching JSON Pairs)/Security/data.json', 'r') as file:
            load = json.load(file)

        password = load['Gpassword']
        # speak("Sir Please Provide Authetication Information")
        user = input("Enter Passkey to access confidential information\n> ")

    if user == password:
        printf("Password access granted\n")
        # path = "C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.7 (Step Towards Organizing)/Security/TTSStoring.txt"
        # write_to_file("Access Granted", path)
        # read_from_file()
        # asyncio.run(speaklong("Welcome Sir"))
        ACCESS_GRANTED.Welcome()
        data.access_point_key()

    else:
        printf("Access denied")
        # speak("Access Denied")
        f = open("C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.7 (Step Towards Organizing)/Security/Denied_Access.txt", "a")
        f.write(user + "\n")

    print("Feedback Saved")