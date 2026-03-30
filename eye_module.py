import numpy as np

def get_eye_aspect_ratio(landmarks):
    # Using approximate eye points (MediaPipe indices)
    try:
        left_eye = [landmarks[33], landmarks[160], landmarks[158],
                    landmarks[133], landmarks[153], landmarks[144]]

        def dist(a, b):
            return np.linalg.norm(np.array([a.x, a.y]) - np.array([b.x, b.y]))

        ear = (dist(left_eye[1], left_eye[5]) + dist(left_eye[2], left_eye[4])) / (2.0 * dist(left_eye[0], left_eye[3]))
        return ear
    except:
        return 0.3