import os
import warnings
import json
from transformers import pipeline

# 1. Suppress Deprecation and Future Warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=FutureWarning)

# 2. Load the question-answer data from a JSON file
def load_question_answer_data(json_file_path):
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # Load JSON data
    return data

def feedback(feedback):
    f = open("C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.7 (Step Towards Organizing)/Data/TrainingData/data.txt", "a")
    f.write(f"{feedback}\n")
    f.close()

# Specify the JSON file path
json_file_path = 'C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 1.7 (Step Towards Organizing)/Data/IntelligenceSupportData.json'
qa_data = load_question_answer_data(json_file_path)

# 3. Function to get an answer based on a question
def get_answer_from_json(question):
    question = question.lower()  # Make the input question lowercase to handle case sensitivity
    for key in qa_data:
        if key.lower() in question:  # Check if any key (question) is a substring of the input
            return qa_data[key]
    returningvar = "Sorry, I don't have an answer for that."
    return returningvar  # Return this if no match is found

# # Example usage
# question = "Can you tell me the time?"  # Replace this with any user input
# answer = get_answer_from_json(question)
# print("Answer:", answer)
