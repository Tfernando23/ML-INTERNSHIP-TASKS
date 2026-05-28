TASK 1: Decision Tree

The objective of this task is to build and visualize a Decision Tree model using machine learning techniques to classify or predict outcomes based on a given dataset. A Decision Tree is a supervised learning algorithm that is widely used for both classification and regression tasks. It works by splitting the dataset into smaller subsets based on feature values, forming a tree-like structure of decisions.

In this task, the process begins with selecting a dataset such as the Iris dataset, which contains features like sepal length, sepal width, petal length, and petal width. These features are used to classify different species of flowers. The dataset is divided into training and testing sets to ensure that the model can generalize well to unseen data.

The Decision Tree model is built using the Scikit-learn library. During training, the algorithm selects the best features to split the data based on criteria such as Gini Index or Entropy. These measures help determine how well a feature separates the data into distinct classes. The tree grows by recursively splitting the data until a stopping condition is met, such as a maximum depth or minimum number of samples per leaf node.

Once the model is trained, predictions are made on the test dataset. The model’s performance is evaluated using metrics such as accuracy, precision, recall, and F1-score. Accuracy measures how many predictions are correct, while the classification report provides deeper insights into the model’s performance for each class.

A key part of this task is visualization. The trained Decision Tree is visualized using plotting functions, which display the structure of the tree. Each node represents a decision based on a feature, and branches represent possible outcomes. Visualization helps in understanding how the model makes decisions and which features are most important.

The main advantage of Decision Trees is their interpretability. Unlike complex models, Decision Trees are easy to understand and explain. However, they can suffer from overfitting if the tree becomes too deep. Techniques such as pruning or setting a maximum depth help control this issue.

Overall, this task demonstrates the complete workflow of a machine learning model—from data preparation and training to evaluation and visualization. It provides a strong foundation for understanding supervised learning and model interpretability.

OUTPUT:

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



