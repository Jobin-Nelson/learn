# Basics

- **Artificial Intelligence**: The effort to automate intellectual tasks normally performed by humans. It can be simple or complex, it could be hard coded rules or complex algorithms.

- **Machine Learning**: In machine learning it tries to figure out the rules for us so that we don't need to hard code it ourselves, so rather than giving program the rules, an algorithm finds the rules for us.
	- Data & Rules -> classical programming -> Answers
	- Data & Answers -> Machine learning -> Rules

- **Neural Network**: A form of machine learning that uses layered representation of data

## Different types of machine learning

- Unsupervised learning
- Supervised learning
- Reinforcemnet learning

# Tensorflow

It is the largest machine learning open source library maintained and supported by Google. Tensorflow has two main components.
- Graphs
- Sessions

Tensorflow works by building a graph of defined computations. Nothing is computed or stored in this graph. It is simply a way of defining the operations that have been written in code.

A tensorflow session allows parts of the graph to be executed. It allocates memory and resources and handles the execution of the operations and computations we've defined.

In some instances we would need to run a session to be able to exectute parts of the graphs we've created earlier.

## Tensors

A tensor is a generalization of vectors and matrices to potentially higher dimensions. Internally, TensorFlow represents tensors as n-dimensional arrays of base datatypes.

# Computer Vision
It is the process of training a computer to do operation like image classification, or image segmentation on image datasets

- The nerual networks that are best at this task is called convolutional neural network CNN for short
- In CNN, there are two main componenets base and head
- Base extracts featues from the image and head classfies the processed features from the base 

The goal of the network during training is to learn two things:
- which features to extract from an image (base).
- which class goes with what features (head).

Using a pretrained base model with an untrained head is called *transfer learning*