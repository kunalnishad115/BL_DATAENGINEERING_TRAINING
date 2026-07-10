from langchain_cohere import CohereEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

docs=[
   "Delhi is the capital of India.",
    "Paris is the capital of France."
]
query='What is The Capital of India'

embedding=CohereEmbeddings(model="embed-english-v3.0")

docs_embedding=embedding.embed_documents(docs)
query_embedding=embedding.embed_query(query)

scores = cosine_similarity([query_embedding], docs_embedding)[0]

for doc, score in zip(docs, scores):
    print(f"Document: {doc}")
    print(f"Similarity: {score:.4f}")
    print("-" * 40)

best_idx = scores.argmax()

print("\nMost Similar Document:")
print(docs[best_idx])
print(f"Score: {scores[best_idx]:.4f}")



