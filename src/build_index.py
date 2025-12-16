import pandas as pd
import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load data
df = pd.read_csv("data/assessments.csv")

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Combine relevant text columns
texts = (
    df["assessment_name"] + " " +
    df["skills"] + " " +
    df["description"]
).tolist()


# Generate embeddings
embeddings = model.encode(texts)

# Create FAISS index
dimension = embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(embeddings)

# Save index
faiss.write_index(index, "data/index.faiss")

# Save metadata
metadata = df.to_dict(orient="records")
with open("data/metadata.pkl", "wb") as f:
    pickle.dump(metadata, f)

print("Vector index and metadata created successfully")
