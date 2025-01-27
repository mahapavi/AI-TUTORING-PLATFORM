from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Mock user study data
user_progress = [
    [5, 3, 0, 0, 2],  # User A's progress
    [1, 0, 3, 4, 0],  # User B's progress
    [0, 5, 1, 0, 3]   # User C's progress
]

# Generate similarity
similarity_matrix = cosine_similarity(user_progress)

def recommend(user_index):
    similar_users = similarity_matrix[user_index].argsort()[::-1][1:]  # Exclude user self
    recommendations = [f"Recommended Topic {i}" for i in similar_users[:3]]
    return recommendations
