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
