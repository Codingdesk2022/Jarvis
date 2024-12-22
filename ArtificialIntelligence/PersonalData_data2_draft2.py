import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from Utils.SpeechDrive import *


# Function to load data from a JSON file
def load_data_from_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

# Load the data from the file
data = load_data_from_file('C:/Users/Infort/OneDrive/Documents/Confidentials/Jarvis 2.0 (Advance Pairing)/ArtificialIntelligence/data2.json')

# Flatten the JSON data to create a list of (question, answers)
qa_pairs = []
for question, answers in data.items():
    for answer in answers:
        qa_pairs.append({"question": question, "answer": answer})

# Convert to list of questions and answers
questions = [pair["question"] for pair in qa_pairs]
answers = [pair["answer"] for pair in qa_pairs]

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Function to get the best answer for a question
def get_best_answer(user_question):
    # Add the user's question to the list of questions for similarity calculation
    questions_with_user_question = questions + [user_question]
    
    # Fit and transform the questions (including the user's question)
    tfidf_matrix = vectorizer.fit_transform(questions_with_user_question)
    
    # Calculate cosine similarities between the user's question and all stored questions
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Get the index of the most similar question
    most_similar_index = similarity_scores.argmax()
    
    # If similarity is too low, return a fallback message
    if similarity_scores[0, most_similar_index] < 0.2:  # Adjust threshold as needed
        return "Sorry, I don't have data about that."
    
    # Return the corresponding answer
    return answers[most_similar_index]

# Main loop for continuous questioning
def getanswer(question):
    user_question = question
        
    # # If the user types 'exit', break the loop
    # if user_question.lower() == "exit":
    #     print("Goodbye!")
        
    # Get the best answer from the data
    answer = get_best_answer(user_question)
        
    print(f"{answer}")
    speak(f"{answer}")

# Run the main function
if __name__ == "__main__":
    getanswer()
