def predict_focus(ear, head_pose):
    if head_pose != "center":
        return "Distracted"
    elif ear < 0.25:
        return "Sleepy"
    else:
        return "Focused"