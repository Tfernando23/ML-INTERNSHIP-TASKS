# TASK 2: Sentiment Analysis

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

# Sample dataset
data = {
    "review": [
        "I love this product", "Amazing experience", "Very happy",
        "Best purchase ever", "Excellent quality", "Superb item",
        "I hate this", "Worst product", "Very bad experience",
        "Not worth it", "Terrible", "Disappointed"
    ],
    "sentiment": [1,1,1,1,1,1, 0,0,0,0,0,0]
}

df = pd.DataFrame(data)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    df["review"], df["sentiment"],
    test_size=0.2,
    random_state=42,
    stratify=df["sentiment"]  
)

# TF-IDF
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Prediction
y_pred = model.predict(X_test_vec)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))