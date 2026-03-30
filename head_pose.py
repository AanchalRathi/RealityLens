import numpy as np

def get_head_pose(landmarks):
    nose = landmarks[1]
    if nose.x < 0.4:
        return "left"
    elif nose.x > 0.6:
        return "right"
    else:
        return "center"