This Data Structures Implementation

This repository contains implementations of various data structures along with test cases to validate their correctness. Each data structure is implemented from scratch to understand their internal workings, efficiency, and use cases.

Table of Contents

Introduction

Implemented Data Structures

Technologies Used

Project Structure

Setup Instructions

Testing

Contributing

License

Introduction

Understanding data structures is fundamental for writing efficient code and solving complex problems. This repository provides implementations of common data structures, focusing on:

Correctness

Performance

Real-world use cases

Each implementation includes:

A well-structured class or module

Methods with proper documentation

Unit tests to verify correctness

Implemented Data Structures

The following data structures are implemented:

Linear Data Structures

Arrays

Linked Lists (Singly, Doubly, Circular)

Stacks

Queues (Simple, Circular, Priority)

Non-Linear Data Structures

Trees (Binary Tree, BST, AVL, Heap, Trie)

Graphs (Adjacency List, Adjacency Matrix)

Hashing

Hash Tables (Custom Implementation)

Bloom Filters

Other Advanced Data Structures

Heaps (MinHeap, MaxHeap, Fibonacci Heap)

Disjoint Sets (Union-Find)

Tries

Suffix Trees

Skip Lists

Technologies Used

Programming Language: Java / Python / C++ (choose your primary language)

Testing Framework: JUnit / PyTest / Google Test (depending on language)

Build Tools: Gradle / Maven (for Java), Makefile (for C++), Virtual Environments (for Python)

Project Structure

📂 data-structures-repo
 ┣ 📂 src
 ┃ ┣ 📂 linear
 ┃ ┃ ┣ 📜 Array.java
 ┃ ┃ ┣ 📜 LinkedList.java
 ┃ ┃ ┣ 📜 Stack.java
 ┃ ┃ ┗ 📜 Queue.java
 ┃ ┣ 📂 non-linear
 ┃ ┃ ┣ 📜 BinaryTree.java
 ┃ ┃ ┣ 📜 Graph.java
 ┃ ┃ ┗ 📜 Trie.java
 ┃ ┣ 📂 hashing
 ┃ ┃ ┣ 📜 HashTable.java
 ┃ ┃ ┗ 📜 BloomFilter.java
 ┣ 📂 tests
 ┃ ┣ 📜 TestArray.java
 ┃ ┣ 📜 TestLinkedList.java
 ┃ ┣ 📜 TestGraph.java
 ┣ 📜 README.md
 ┣ 📜 .gitignore
 ┣ 📜 LICENSE

Setup Instructions

Clone the repository:

git clone https://github.com/yourusername/data-structures.git
cd data-structures

Install dependencies (if required):

# Java (Gradle)
./gradlew build

# Python
pip install -r requirements.txt

# C++
make

Testing

To ensure correctness, each data structure has associated unit tests.
Run tests using:

# Java
./gradlew test

# Python
pytest tests/

# C++
make test

Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

How to Contribute:

Fork the repository

Create a new branch (git checkout -b feature-name)

Commit your changes (git commit -m 'Add feature')

Push to the branch (git push origin feature-name)

Open a Pull Request

License

This project is licensed under the MIT License - see the LICENSE file for details.


