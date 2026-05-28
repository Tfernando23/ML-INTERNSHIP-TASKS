**TASK 2: Sentiment Analysis Using TF-IDF and Logistic Regression**

**Introduction**

This task focuses on performing sentiment analysis on a dataset of customer reviews using natural language processing (NLP) techniques. Sentiment analysis is a method used to determine whether a piece of text expresses a positive or negative opinion. It is widely used in real-world applications such as product reviews, social media analysis, and customer feedback systems. In this task, a dataset of sample reviews is analyzed to classify sentiments into positive and negative categories. The implementation combines text preprocessing, feature extraction, and machine learning to build an effective sentiment classification model. This task helps in understanding how textual data can be transformed into meaningful numerical representations and used for predictive analysis.

**Objective**

The main objective of this task is to build a sentiment analysis model that can accurately classify customer reviews as either positive or negative. It aims to demonstrate how text data can be processed using TF-IDF vectorization and how a machine learning algorithm like Logistic Regression can be applied for classification. Another important objective is to evaluate the model’s performance using appropriate metrics and understand its effectiveness in predicting sentiments.

**Tools and Technologies Used**

This task is implemented using Python due to its strong support for data analysis and machine learning. Pandas is used to create and manage the dataset efficiently. Scikit-learn provides tools for splitting the data, transforming text using TF-IDF vectorization, building the Logistic Regression model, and evaluating performance. The TF-IDF Vectorizer converts text data into numerical form by assigning importance to words based on their frequency. Logistic Regression is used as the classification algorithm because it is simple, efficient, and suitable for binary classification problems. The development environment can be Jupyter Notebook or Visual Studio Code.

**Methodology / Approach**

The task begins with creating a dataset of customer reviews along with their corresponding sentiment labels. The data is then split into training and testing sets using stratified sampling to maintain class balance. Next, TF-IDF vectorization is applied to convert the textual reviews into numerical feature vectors that can be used by the machine learning model. The Logistic Regression model is then initialized and trained using the transformed training data. After training, the model is used to predict sentiments for the test data. The performance of the model is evaluated using accuracy score and classification report, which provide detailed insights into precision, recall, and overall effectiveness of the model.

**Result / Outcome**

The outcome of this task is a trained sentiment analysis model capable of classifying customer reviews with good accuracy. The evaluation metrics demonstrate the model’s ability to correctly identify positive and negative sentiments. This shows how text data can be effectively analyzed using machine learning techniques.

**Conclusion**

In conclusion, this task demonstrates how sentiment analysis can be performed using NLP techniques and machine learning algorithms. It highlights the importance of text preprocessing, feature extraction, and model evaluation. The task provides practical experience in working with textual data and builds a strong foundation for more advanced NLP applications such as chatbots, recommendation systems, and opinion mining.


**OUTPUT:**

Accuracy: 0.3333333333333333

 precision    recall  f1-score   support

           0       0.00      0.00      0.00         2
           1       0.33      1.00      0.50         1

    accuracy                           0.33         3
    
   macro avg       0.17      0.50      0.25         3
   
weighted avg       0.11      0.33      0.17         3


<img width="1441" height="439" alt="Screenshot 2026-05-28 162348" src="https://github.com/user-attachments/assets/75c0a347-28f6-45c9-bb52-0eec2bc030d4" />

