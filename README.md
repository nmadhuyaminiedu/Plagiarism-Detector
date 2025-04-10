# 🧠 Plagiarism Detector Web App

This project is an intelligent web-based system that leverages Natural Language Processing (NLP) and Machine Learning to detect potential plagiarism in user-submitted content. Designed for simplicity and functionality, the system provides a responsive web interface powered by Flask and a powerful backend model trained on TF-IDF features.
---

## 🚀 Features

- 🌐 Web interface using Flask and HTML/CSS
- 🤖 Machine Learning model using TF-IDF and a binary classifier
- 🔍 Detects whether input text is plagiarized or not
- 📦 CLI support for local testing via `plagiarism_checker.py`

---

## 🗃️ Project Structure

```
.
├── PC_app.py                    # Flask web app
├── plagiarism_checker.py        # Command-line interface version
├── PC_model.pkl                 # Trained ML model (binary classification)
├── PC_tf_idf_vectorizer.pkl     # TF-IDF vectorizer used for training and prediction
├── Plag_dataset.csv             # Dataset used for training (optional, not loaded in scripts)
└── templates/
    └── index.html               # Front-end page for user input and output
```

---

## 🛠️ How to Run

### 🔸 Web App

1. Install dependencies (if needed):
    ```bash
    pip install flask scikit-learn
    ```

2. Run the Flask application:
    ```bash
    python PC_app.py
    ```

3. Open your browser and navigate to:
    ```
    http://127.0.0.1:5000/
    ```

---

### 🔹 CLI Version

1. Run the command-line plagiarism checker:
    ```bash
    python plagiarism_checker.py
    ```

2. Enter text when prompted. Type `exit` to quit.

---

## 📌 Notes

- `PC_model.pkl` and `PC_tf_idf_vectorizer.pkl` must be present in the same directory as the `.py` files.
- The web app renders `index.html` from the `templates/` directory (Flask default). Make sure to keep it there.
- This app is designed for educational and demonstration purposes.

---
