### TASK 1: Decision Tree – Iris Dataset Classification

#### Introduction

This task focuses on building and visualizing a Decision Tree model using Scikit-learn to classify outcomes from a dataset. A decision tree is a supervised machine learning algorithm used for both classification and regression tasks. It works by splitting the dataset into smaller subsets based on feature values, forming a tree-like structure of decisions. In this task, the well-known Iris dataset is used, which contains measurements of different flower species. The goal is to understand how a decision tree can be trained to accurately classify different categories based on input features. This task provides a strong foundation in machine learning by combining data handling, model training, evaluation, and visualization.

#### Objective

The primary objective of this task is to implement a Decision Tree Classifier that can accurately predict the class of iris flowers based on their features such as sepal length, sepal width, petal length, and petal width. The task also aims to visualize the structure of the trained decision tree to better understand how decisions are made within the model. Additionally, it focuses on evaluating the performance of the model using appropriate metrics to ensure its effectiveness.

#### Tools and Technologies Used

This task is implemented using Python as the programming language. Several libraries are used to achieve the objective. NumPy and Pandas are utilized for handling and managing data efficiently. Scikit-learn provides the built-in Iris dataset, along with tools for splitting the data, building the decision tree model, and evaluating its performance. Matplotlib is used to visualize the decision tree, making it easier to interpret the model’s decision-making process. The development environment can be Jupyter Notebook or any Python IDE such as Visual Studio Code.

#### Methodology / Approach

The task begins with loading the Iris dataset using Scikit-learn. The dataset is divided into input features (X) and target labels (y). Next, the data is split into training and testing sets using the train_test_split function to ensure that the model is evaluated on unseen data. A Decision Tree Classifier is then created with a specified maximum depth to control the complexity of the model and avoid overfitting. The model is trained using the training dataset. After training, predictions are made on the test dataset. The model’s performance is evaluated using accuracy score and classification report, which provide insights into how well the model is performing. Finally, the trained decision tree is visualized using a plot, which clearly shows how the model makes decisions based on different feature conditions.

#### Result / Outcome

The result of this task is a trained decision tree model capable of classifying iris flowers into their respective categories with good accuracy. The evaluation metrics indicate the effectiveness of the model, while the visualization provides a clear understanding of the decision-making process. This helps in interpreting how different features influence the classification.

#### Conclusion

In conclusion, this task demonstrates how a Decision Tree model can be implemented and visualized for classification problems. It highlights the importance of data splitting, model training, evaluation, and visualization in machine learning workflows. The task provides practical experience in using Scikit-learn and helps build a strong understanding of how decision trees work, making it a valuable step toward more advanced machine learning concepts.

**OUTPUT:**

Accuracy: 1.0

              precision    recall  f1-score   support

           0       1.00      1.00      1.00        10
           1       1.00      1.00      1.00         9
           2       1.00      1.00      1.00        11

    accuracy                           1.00        30
    
   macro avg       1.00      1.00      1.00        30
   
weighted avg       1.00      1.00      1.00        30


<img width="924" height="240" alt="Screenshot 2026-05-28 162335" src="https://github.com/user-attachments/assets/eeee56d4-423b-45db-aef2-1da4b2f5703d" />





<img width="1920" height="1080" alt="Screenshot 2026-05-24 174952" src="https://github.com/user-attachments/assets/6b63eeaa-a209-45c7-9356-5d2df595522f" />



