import pickle

# Load the trained model
with open("PC_model.pkl", "rb") as f:
    model = pickle.load(f)

# Load the TF-IDF vectorizer
with open("PC_tf_idf_vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

print("✅ Model and vectorizer loaded successfully!")

# Prediction loop
while True:
    input_text = input("\n📝 Enter text to check for plagiarism (or type 'exit' to quit):\n> ")

    if input_text.lower() == "exit":
        print("👋 Exiting plagiarism checker.")
        break

    # Vectorize and predict
    X_input = vectorizer.transform([input_text])
    y_pred = model.predict(X_input)

    # Output result
    if y_pred[0] == 1:
        print("🚨 Plagiarism Detected!")
    else:
        print("✅ No Plagiarism Detected.")