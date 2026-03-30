import cv2
from face_module import get_face_landmarks
from eye_module import get_eye_aspect_ratio
from head_pose import get_head_pose
from focus_model import predict_focus

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    landmarks = get_face_landmarks(frame)

    if landmarks is not None:
        ear = get_eye_aspect_ratio(landmarks)
        head_pose = get_head_pose(landmarks)

        focus = predict_focus(ear, head_pose)

        cv2.putText(frame, f"Focus: {focus}", (20, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("RealityLens", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()