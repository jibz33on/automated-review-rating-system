
import streamlit as st
import joblib
import numpy as np
from scipy.sparse import hstack

# Load saved model and vectorizer
model = joblib.load('../models/linear_regression_model.pkl')
tfidf = joblib.load('../models/tfidf_vectorizer.pkl')

# App configuration
st.set_page_config(page_title="Review Score Predictor", page_icon="📝")
st.title("📝 Review Score Predictor")
st.write("Enter a review and we'll predict the review score using a trained Linear Regression model.")

# User input: Review text only
review_text = st.text_area("✍️ Enter your review text here", height=150)

if st.button("Predict Score"):
    if review_text.strip() == "":
        st.warning("Please enter some review text to continue.")
    else:
        # Derive numeric features from text
        review_length_words = len(review_text.split())
        review_length_chars = len(review_text)
        helpfulness_ratio = 0.5  # Default neutral value

        # TF-IDF transformation
        text_vector = tfidf.transform([review_text])

        # Numeric feature vector
        numeric_vector = np.array([[review_length_words, review_length_chars, helpfulness_ratio]])

        # Combine text + numeric
        full_vector = hstack([text_vector, numeric_vector])

        # Predict
        predicted_score = model.predict(full_vector)[0]

        # Interpret result
        if predicted_score < 2.5:
            sentiment = "😞 Negative"
        elif predicted_score < 3.5:
            sentiment = "😐 Neutral"
        elif predicted_score < 5.0:
            sentiment = "🙂 Positive"
        else:
            sentiment = "😄 Very Positive"

        # Display result
        st.success(f"🎯 Predicted Review Score: {predicted_score:.2f}")
        st.info(f"🧠 Interpretation: {sentiment}")

