import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --------------------------------------------------
# Load dataset safely (works from any directory)
# --------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "..", "data", "assessments.csv")

data = pd.read_csv(DATA_PATH)

# --------------------------------------------------
# Combine important text features
# --------------------------------------------------

data["combined_features"] = (
    data["job_role"] + " " +
    data["skills"] + " " +
    data["experience_level"] + " " +
    data["description"]
)

# --------------------------------------------------
# Convert text to numerical vectors using TF-IDF
# --------------------------------------------------

vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(data["combined_features"])

# --------------------------------------------------
# Recommendation function
# --------------------------------------------------

def recommend_assessments(job_role, skills, experience_level, top_n=3):
    user_input = job_role + " " + skills + " " + experience_level
    user_vector = vectorizer.transform([user_input])

    similarity_scores = cosine_similarity(user_vector, feature_vectors).flatten()
    top_indices = similarity_scores.argsort()[-top_n:][::-1]

    return data.iloc[top_indices][["assessment_name", "description"]]

# --------------------------------------------------
# Run example
# --------------------------------------------------

if __name__ == "__main__":
    recommendations = recommend_assessments(
        job_role="Software Engineer",
        skills="Python Problem Solving",
        experience_level="Fresher"
    )

    print("\nRecommended Assessments:\n")
    print(recommendations.to_string(index=False))
