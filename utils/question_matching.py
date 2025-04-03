import json
import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def find_similar_question(input_question):
    """Find the most similar question from questions.json based on TF-IDF similarity."""
    
    # Get the absolute path to `questions.json`
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "..", "data", "questions.json")

    # ✅ Handle missing/corrupt JSON files
    try:
        with open(file_path, "r") as f:
            questions_json = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"❌ Error: {file_path} not found!")
    except json.JSONDecodeError:
        raise ValueError(f"❌ Error: Invalid JSON format in {file_path}")

    if not questions_json:
        raise ValueError("❌ Error: The questions.json file is empty!")

    # Extract question keys and descriptions
    question_keys = list(questions_json.keys())
    question_descriptions = [questions_json[key]["description"] for key in question_keys]

    # Vectorize questions
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(question_descriptions)
    input_question_vector = vectorizer.transform([input_question])

    # Compute cosine similarity
    cosine_similarities = cosine_similarity(input_question_vector, tfidf_matrix).flatten()
    most_similar_question_index = np.argmax(cosine_similarities)

    # Get the best match
    most_similar_question = question_keys[most_similar_question_index]
    most_similar_question_description = question_descriptions[most_similar_question_index]

    return most_similar_question, most_similar_question_description


# ✅ Example Usage
if __name__ == "__main__":
    question, description = find_similar_question("i want to create a HTTP request with uv?")
    print("🔹 Matched Question:", question)
    print("🔹 Description:", description)
