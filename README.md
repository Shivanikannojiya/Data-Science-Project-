# Data-Science-Project-
# 🚚 E-Commerce Product Delivery Prediction

This project predicts whether an e-commerce product will be delivered **on time or late** using machine learning.

## 🧠 Goal
To help e-commerce companies identify **high-risk deliveries** before dispatch and improve **customer satisfaction**.

## 📊 Dataset
- 10,999 rows, 12 features
- Target: `Reached on Time` (1 = Yes, 0 = No)

## 🔧 Features Used
- Mode of Shipment
- Customer Rating
- Cost of Product
- Product Importance
- Discount Offered
- Weight (in grams), etc.

## 🧹 Preprocessing
- Removed missing values
- Label encoding for categorical columns
- Normalization of features

## 🤖 Models Tried
- Logistic Regression
- Decision Tree
- Random Forest
- ✅ K-Nearest Neighbors (**Best Accuracy: 78.2%**)

## 🚀 Deployment
Model deployed using **Streamlit** for real-time prediction.

## 📌 Tech Stack
Python, Pandas, Scikit-learn, Matplotlib, Seaborn, Streamlit

## 📈 Result
KNN was the most accurate model. The app can help businesses plan logistics and reduce delays.
