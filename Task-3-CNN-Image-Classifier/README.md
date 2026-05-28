**TASK 3: Convolutional Neural Network (CNN) for Image Classification using MNIST Dataset**

**Introduction**

This task focuses on building and implementing a Convolutional Neural Network (CNN) for image classification using the MNIST dataset. CNNs are a class of deep learning models specifically designed for processing structured grid data such as images. They are widely used in computer vision tasks due to their ability to automatically detect important features like edges, textures, and patterns. In this task, the MNIST dataset, which consists of handwritten digit images, is used to train a model that can accurately recognize digits from 0 to 9. This task provides practical exposure to deep learning concepts and demonstrates how neural networks can be applied to solve image classification problems.

**Objective**

The main objective of this task is to design and train a CNN model that can accurately classify handwritten digit images into their respective categories. It aims to demonstrate how convolutional layers, pooling layers, and fully connected layers work together to extract features and perform classification. Another objective is to evaluate the performance of the trained model on test data and understand its accuracy and reliability.

**Tools and Technologies Used**

This task is implemented using Python with TensorFlow and Keras as the primary deep learning frameworks. TensorFlow provides efficient tools for building and training neural networks, while Keras offers a high-level API for creating models easily. The MNIST dataset is loaded directly from Keras datasets. Matplotlib can be used for visualizing data and training performance. The development environment can be Jupyter Notebook or Visual Studio Code, which allows easy experimentation and debugging.

**Methodology / Approach**

The task begins by loading the MNIST dataset, which contains grayscale images of handwritten digits along with their labels. The data is then normalized by scaling pixel values to a range between 0 and 1 to improve model performance. The images are reshaped to include a channel dimension, making them compatible with the CNN input format. The model is built using a sequential architecture consisting of convolutional layers to extract features, followed by max-pooling layers to reduce dimensionality and computational complexity. The extracted features are then flattened and passed through dense layers to perform classification. The final layer uses a softmax activation function to output probabilities for each digit class. The model is compiled using the Adam optimizer and sparse categorical cross-entropy loss function. It is then trained on the training dataset for multiple epochs while validating on test data. Finally, the model is evaluated on the test dataset to measure its accuracy.

**Result / Outcome**

The outcome of this task is a trained CNN model capable of accurately classifying handwritten digits from the MNIST dataset. The model achieves good accuracy on the test dataset, demonstrating its ability to generalize to unseen data. The performance metrics provide insight into how well the model has learned the patterns in the data.

**Conclusion**

In conclusion, this task demonstrates the implementation of a Convolutional Neural Network for image classification. It highlights the importance of data preprocessing, model architecture design, and performance evaluation in deep learning. This task provides a strong foundation for understanding more advanced topics in computer vision and neural networks, making it a valuable step in learning modern AI techniques.


**OUTPUT:**

Training Accuracy (final epoch):99.36%

Validation Accuracy:98.98%

Test Accuracy:98.98%

Test Loss:0.0309


<img width="1437" height="587" alt="Screenshot 2026-05-28 162504" src="https://github.com/user-attachments/assets/490c36f8-8887-4782-8148-72ac4a641a46" />


