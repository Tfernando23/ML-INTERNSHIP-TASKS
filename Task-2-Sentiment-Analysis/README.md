TASK 2: Sentiment Analysis

The goal of this task is to perform sentiment analysis on a dataset of customer reviews using Natural Language Processing (NLP) techniques. Sentiment analysis is the process of determining whether a piece of text expresses a positive, negative, or neutral sentiment. It is widely used in applications such as product reviews, social media monitoring, and customer feedback analysis.

The first step in this task involves collecting or creating a dataset of textual data, typically consisting of customer reviews and corresponding sentiment labels (positive or negative). Since machine learning models cannot directly process text, preprocessing is required to clean and transform the text into a usable format.

Text preprocessing includes steps such as converting text to lowercase, removing punctuation, eliminating stopwords (common words like “and”, “the”), and tokenization (splitting text into words). These steps help reduce noise and improve the quality of the data.

The next step is feature extraction using TF-IDF (Term Frequency-Inverse Document Frequency). TF-IDF converts textual data into numerical vectors by measuring how important a word is in a document relative to the entire dataset. Words that appear frequently in a specific document but not across all documents receive higher importance.

Once the text is transformed into numerical form, a Logistic Regression model is used for classification. Logistic Regression is a supervised learning algorithm commonly used for binary classification problems. It predicts the probability of a text belonging to a particular class (positive or negative sentiment).

The dataset is split into training and testing sets. The model is trained on the training data and evaluated on the test data. Performance metrics such as accuracy, precision, recall, and F1-score are used to assess the model’s effectiveness.

The results of the model provide insights into how well it can classify sentiments. For example, a high accuracy indicates that the model correctly predicts most sentiments. However, additional metrics like precision and recall are important when dealing with imbalanced datasets.

This task highlights the importance of text preprocessing and feature engineering in NLP. It also demonstrates how machine learning can be applied to real-world problems involving unstructured data. Sentiment analysis plays a crucial role in businesses by helping them understand customer opinions and improve their products and services.

OUTPUT:

Accuracy: 0.3333333333333333

 precision    recall  f1-score   support

           0       0.00      0.00      0.00         2
           1       0.33      1.00      0.50         1

    accuracy                           0.33         3
    
   macro avg       0.17      0.50      0.25         3
   
weighted avg       0.11      0.33      0.17         3


<img width="1441" height="439" alt="Screenshot 2026-05-28 162348" src="https://github.com/user-attachments/assets/75c0a347-28f6-45c9-bb52-0eec2bc030d4" />

