import streamlit as st
import joblib

# Load model
model = joblib.load("spam_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

# Streamlit UI
st.title("📧 Spam Detector")
user_input = st.text_input("Enter a message:")

if user_input:
    # Predict
    input_vec = tfidf.transform([user_input])
    prediction = model.predict(input_vec)[0]
    
    # Display result
    if prediction == 1:
        st.error("🚨 Spam!")
    else:
        st.success("✅ Not Spam!")