**TASK 4: Recommendation System using Collaborative Filtering (SVD)**

**Introduction**
This task focuses on building a recommendation system using collaborative filtering techniques, specifically matrix factorization through the Singular Value Decomposition (SVD) algorithm. Recommendation systems are widely used in real-world applications such as e-commerce platforms, streaming services, and online marketplaces to suggest relevant items to users based on their preferences. In this task, user-item interaction data is analyzed to predict ratings and generate personalized recommendations. By implementing SVD using the Surprise library, this task demonstrates how machine learning can effectively model user behavior and improve recommendation accuracy.

**Objective**
The primary objective of this task is to develop a recommendation system that can predict user ratings for items using collaborative filtering. It aims to demonstrate how matrix factorization techniques like SVD can uncover hidden patterns in user-item interactions. Another key objective is to evaluate the performance of the model using appropriate metrics and ensure that the recommendations generated are meaningful and accurate. Additionally, the task focuses on generating predicted ratings for a specific user to showcase personalized recommendation results.

**Tools and Technologies Used**
This task is implemented using Python along with the Surprise library, which provides specialized tools for building recommendation systems. Pandas is used to create and manage the dataset containing users, items, and ratings. The Reader class defines the rating scale, while the Dataset module converts the data into a format suitable for training. The SVD algorithm is used as the core model for collaborative filtering. The model’s performance is evaluated using Root Mean Squared Error (RMSE), which measures prediction accuracy. The development environment can be Jupyter Notebook or Visual Studio Code.

**Methodology / Approach**
The process begins by creating a dataset consisting of user-item-rating interactions. This data is converted into a structured format using Pandas and then loaded into the Surprise framework. The dataset is split into training and testing sets to ensure proper model evaluation. The SVD model is initialized and trained on the training dataset, where it learns latent features representing user preferences and item characteristics. After training, the model is tested on unseen data to generate predictions. The accuracy of these predictions is evaluated using RMSE. Finally, the trained model is used to predict ratings for a specific user across multiple items, enabling the system to recommend items with higher predicted ratings.

**Result / Outcome**
The outcome of this task is a functional recommendation system capable of predicting user preferences with reasonable accuracy. The RMSE value provides insight into how closely the predicted ratings match actual values. The system successfully generates personalized recommendations by estimating ratings for items not yet interacted with by the user.

**Conclusion**
In conclusion, this task demonstrates the implementation of a recommendation system using collaborative filtering and matrix factorization techniques. It highlights how user behavior data can be leveraged to generate personalized suggestions. The use of the SVD algorithm and Surprise library simplifies the development process while maintaining effectiveness. This task provides a strong foundation for understanding real-world recommendation systems and their applications in various domains.


**OUTPUT:**
RMSE: 0.2989

Predicted rating for Item1: 4.537946505813056

Predicted rating for Item2: 4.2391930895669265

Predicted rating for Item3: 4.4093633469229925


<img width="1023" height="112" alt="Screenshot 2026-05-28 162555" src="https://github.com/user-attachments/assets/5230884f-562b-4918-aadf-ef484eba6aae" />

