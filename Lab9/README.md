# Lab 9: Object-Oriented Programming and Operator Overloading in Python

## Overview
In Lab 9, we delve deep into Python's object-oriented programming capabilities to implement sophisticated systems and functionalities. This lab includes creating a dispatch dictionary for a parking meter system, simulating a digital clock, and performing operations on time objects through method and operator overloading. These exercises showcase the power of Python's OOP features for building complex and efficient software solutions.

## Objectives
- Explore Python's object-oriented programming features to encapsulate data and behaviors into classes and objects.
- Implement dispatch dictionaries to handle message passing and dynamic method invocation.
- Utilize operator overloading to enable arithmetic and string operations on custom objects.
- Demonstrate the use of class methods, static methods, and instance methods to manipulate and present data in meaningful ways.

## Exercises Overview and Solutions

### 1. Parking Meter System with Dispatch Dictionary
- Implemented a flexible parking meter system using a dispatch dictionary, enabling operations like charging the meter, parking time tracking, and querying the remaining balance. This approach demonstrates handling dynamic method calls and managing state within an object without traditional method definitions.
- Example enhancements include transitioning the dispatch dictionary implementation to a class-based approach, highlighting Python's versatility in object management.

### 2. Digital Clock Simulation
- Developed a `Time` class to simulate a digital clock that supports setting and retrieving time, advancing time by seconds, and calculating the total seconds since midnight. This class demonstrates Python's capability to encapsulate related data and functionality within a coherent structure, making time manipulations intuitive and straightforward.

### Operator Overloading for Time Manipulation
- Extended the `Time` class with operator overloading to support adding and subtracting time objects or adjusting time by seconds. This feature showcases how to make custom objects work seamlessly with Python's built-in operators for intuitive and readable code.
- Example usage:
  ```python
  start_time = Time(9, 45, 0)
  duration = Time(1, 35, 0)
  end_time = start_time + duration
  print(end_time)  # Output: 11:20:00
  ```

### Enhancing Usability with String Representation and Comparison Methods
- Implemented `__str__` for easy string representation of `Time` objects and comparison methods to logically compare times. These enhancements improve the usability and integration of custom objects with Python's standard library and idioms.

## Conclusion
Lab 9 exemplifies the application of advanced object-oriented programming concepts in Python to create robust and reusable software components. Through encapsulation, polymorphism, and operator overloading, we can build intuitive and efficient systems that leverage Python's dynamic nature and rich feature set.
