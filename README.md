# 🔢 Automated Review Rating System

This project is an AI-powered regression model that predicts a numeric review score based on customer review text. It combines Natural Language Processing (NLP) with machine learning techniques to provide an intelligent way to estimate review ratings automatically.

## 📚 Project Overview

Goal: Predict the review score (1 to 5) based on review content.

Type: Regression problem (not classification)

Interface: Streamlit web application

Best Model Chosen: Linear Regression (after evaluating multiple models)

## 📈 Dataset Summary

The dataset consists of customer reviews and their respective numeric scores (from an e-commerce platform like Amazon).

Features Used:

cleaned_text – Text review content (preprocessed)

review_length_words – Number of words in the review

review_length_chars – Number of characters in the review

helpfulness_ratio – Ratio of helpful votes to total votes

## 🤖 Machine Learning Pipeline

### 1. Text Vectorization

Used TF-IDF Vectorizer with unigrams and bigrams

Limited features to 10,000

### 2. Feature Engineering

Combined TF-IDF vector with numeric features using scipy.hstack

### 3. 📊 Model Comparison (Before Tuning)

| Model             | MAE    | RMSE   | R² Score |
|------------------|--------|--------|----------|
| Linear Regression| 0.6637 | 0.8881 | 0.5420   |
| Ridge Regression | 0.6779 | 0.9043 | 0.5251   |
| XGBoost          | 0.7379 | 0.9879 | 0.4332   |
| Random Forest    | 0.9861 | 1.2399 | 0.1072   |
| Lasso Regression | 1.0376 | 1.3084 | 0.0059   |

### 4. Tuning Performed

Ridge Regression and XGBoost were tuned

Final Chosen Model: Linear Regression (best trade-off of simplicity and accuracy)

## 🌐 Streamlit App

A simple and clean user interface using Streamlit allows users to:

Input review text

Automatically calculate numeric features

Predict the score

#### Example Output:

Input: "This product is amazing! I loved it."
Predicted Score: 4.86

## 💡 How to Run the App Locally

### 1. Clone the Repository

git clone https://github.com/jibz33on/automated-review-rating-system.git
cd automated-review-rating-system/frontend

### 2. Install Requirements

pip install -r ../requirements.txt

### 3. Launch Streamlit App

streamlit run app.py

## 🎨 Project Structure

├── data/                        # Dataset CSVs (ignored in repo)
├── models/                      # Saved model & vectorizer
├── notebooks/                   # Jupyter notebooks (EDA, modeling)
├── frontend/
│   └── app.py                  # Streamlit UI
└── README.md

## 🏆 Future Improvements

Integrate pre-trained models (e.g., BERT)

Add review sentiment classification

Host on Streamlit Cloud for public access

## 🙏 Acknowledgments

Dataset inspiration: Amazon product reviews

Libraries: scikit-learn, streamlit, xgboost, pandas, numpy

### 🔧 Author

Jibin KunjumonGitHub: jibz33on

