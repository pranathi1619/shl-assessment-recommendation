import faiss
import pickle
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load FAISS index
index = faiss.read_index("data/index.faiss")

# Load metadata
with open("data/metadata.pkl", "rb") as f:
    metadata = pickle.load(f)

# User query
query = "Senior Data Analyst with 5 years experience in SQL, Excel and Python"

# Create query embedding
query_embedding = model.encode([query])

# Search top 3 matches
D, I = index.search(query_embedding, k=3)

print("\nRecommended Assessments:")
for idx in I[0]:
    assessment = metadata[idx]
    print("-", assessment["assessment_name"])
