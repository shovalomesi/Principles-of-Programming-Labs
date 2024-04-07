# Lab 8: Advanced Data Management and Operations in Python

## Overview
In Lab 8, we tackle a set of complex problems that require an understanding of mutable data, conventional interfaces, and the use of dispatch functions. These exercises are designed to challenge your ability to think abstractly and implement solutions that are both efficient and readable. By completing these tasks, you'll demonstrate proficiency in managing stateful programs and manipulating data in sophisticated ways.

## Objectives
- Develop a text processing pipeline to analyze and report on text data.
- Implement a banking system using dispatch functions to manage accounts and perform transactions.
- Create functions to compute the cartesian product of sets, introducing conditions to filter the resulting pairs.
- Simulate an electronic parking system that tracks and charges for parking usage dynamically.

## Exercises Overview and Solutions

### 1. Text Processing Pipeline
- Implemented a pipeline for processing text data that includes separating words, filtering out stopwords, and calculating word frequency. Utilized Python's `map`, `filter`, and dictionary comprehensions for efficient data processing.
- Example usage:
  ```python
  stop_list = ('is', 'it', 'a', 'the', 'my', 'and')
  result = text_preprocessing('My cat is 10 and it is a very fat cat', stop_list)
  print(result)  # Output: {'fat': 1, 'very': 1, 'cat': 2}
  ```

### 2. Banking System Simulation
- Created a banking system that allows for account creation, balance inquiry, deposit, withdrawal, and funds transfer between accounts, showcasing the use of dispatch functions to encapsulate and manage account operations.
- The system supports a series of transactions and provides feedback on operations such as insufficient funds or invalid transaction requests.

### 3. Cartesian Product with Conditions
- Developed a set of functions to calculate the cartesian product of two sets and extended it to include conditions for filtering the resulting pairs. This exercise demonstrates the power of lambda functions and higher-order functions in data processing.
- Example usage:
  ```python
  result = cond_c_prod(lambda x: type(x) == int, (1, 2, 3.5), (3, 'a', 4))
  print(result)  # Output: ((1, 3), (1, 4), (2, 3), (2, 4))
  ```

### 4. Electronic Parking System Simulation
- Simulated an electronic parking system where users can load funds onto a parking card, and the system deducts parking charges based on usage. Implemented using dispatch functions, this system handles various commands and responds appropriately to invalid inputs.
- This simulation provides practical insights into the use of message-passing and dispatch functions to create flexible and interactive systems.

## Conclusion
Lab 8 presents a comprehensive exploration of managing mutable data, utilizing dispatch functions for state management, and employing functional programming techniques for data analysis and system simulation. These exercises not only bolster your understanding of Python's capabilities but also prepare you for tackling real-world problems with confidence and creativity.
