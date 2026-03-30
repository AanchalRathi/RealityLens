# RealityLens — Cognitive Load & Focus Detection System

## 🚀 Overview

RealityLens is a real-time Computer Vision system that analyzes a user's facial behavior through a webcam to estimate their focus level and cognitive state.

This project goes beyond traditional face detection by attempting to understand *how engaged a person is*, making it useful in online learning, productivity tracking, and behavioral analytics.

---

## 🧠 Features

* Real-time webcam-based analysis
* Face landmark detection using MediaPipe
* Eye activity estimation (blink/fatigue proxy)
* Head pose tracking (attention direction)
* Focus classification:

  * Focused
  * Distracted
  * Sleepy

---

## ⚙️ Tech Stack

* Python
* OpenCV
* MediaPipe
* NumPy

---

## 📁 Project Structure

```
RealityLens/
│
├── src/
│   ├── main.py
│   ├── face_module.py
│   ├── eye_module.py
│   ├── head_pose.py
│   ├── focus_model.py
│
├── models/
├── data/
├── requirements.txt
└── README.md
```

---

## 🛠️ Installation

```bash
git clone https://github.com/AanchalRathi/RealityLens.git
cd RealityLens
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python src/main.py
```

---

## 🧩 How It Works

1. Webcam captures real-time video
2. Face landmarks are extracted using MediaPipe
3. Eye aspect ratio (EAR) is estimated
4. Head orientation is analyzed
5. A rule-based model predicts focus level

---

## 📊 Future Improvements

* Replace rule-based logic with trained ML model (LSTM)
* Add emotion detection
* Store session analytics
* Build dashboard (Streamlit)

---

## ⚠️ Limitations

* Current model uses simplified heuristics
* Sensitive to lighting conditions
* Not medically accurate

---

## 📚 What I Learned

* Real-time CV pipelines
* Facial landmark processing
* System design for ML applications
* Bridging CV + behavioral analytics

---

## 👨‍💻 Author

Aanchal Rathi
