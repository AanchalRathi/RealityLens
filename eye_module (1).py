import numpy as np

def euclidean(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

def get_eye_aspect_ratio(landmarks):
    # simplified fake EAR (placeholder for demo)
    return np.random.uniform(0.2, 0.35)