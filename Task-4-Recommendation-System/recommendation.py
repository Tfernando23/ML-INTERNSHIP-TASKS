# TASK 4: Recommendation System using Surprise

from surprise import Dataset, Reader
from surprise.model_selection import train_test_split
from surprise import SVD
from surprise import accuracy

# Sample dataset
data = {
    "user": ["A","A","B","B","C","C"],
    "item": ["Item1","Item2","Item1","Item3","Item2","Item3"],
    "rating": [5,4,4,5,3,4]
}

import pandas as pd
df = pd.DataFrame(data)

# Load into Surprise
reader = Reader(rating_scale=(1,5))
dataset = Dataset.load_from_df(df, reader)

trainset, testset = train_test_split(dataset, test_size=0.2)

# Model
model = SVD()
model.fit(trainset)

# Predictions
predictions = model.test(testset)

# Evaluate
accuracy.rmse(predictions)

# Recommend for user A
for item in ["Item1", "Item2", "Item3"]:
    pred = model.predict("A", item)
    print(f"Predicted rating for {item}: {pred.est}")