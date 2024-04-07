# Lab 11: Generic Functions and Operator Overloading in Python

## Overview
Lab 11 introduces the concept of generic functions and operator overloading to perform arithmetic operations across different data types, specifically focusing on rational and complex numbers. The lab exercises guide you through implementing a system that supports adding, subtracting, multiplying, and dividing these numbers in a type-agnostic manner. By leveraging Python's capabilities for operator overloading and data-directed programming, you'll create a versatile and powerful arithmetic system.

## Objectives
- Implement generic functions that can apply arithmetic operations to various data types by using a centralized method dispatch system.
- Utilize operator overloading to make arithmetic operations between custom data types intuitive and Pythonic.
- Explore data-directed programming to extend the arithmetic system in a modular and scalable way.

## Exercises Overview and Solutions

### 1. Building a Generic Add Function
- Developed a generic `add` function capable of handling arithmetic operations between rational and complex numbers by utilizing a dispatch dictionary. This system dynamically selects the appropriate operation based on the types of the operands.

### 2. Extending the System with Subtraction
- Integrated subtraction into the arithmetic system by defining generic operations and extending the dispatch dictionary. This allows for the subtraction of complex numbers and rational numbers with proper type handling and conversion.

### 3. Operator Overloading for Basic Arithmetic Operations
- Overloaded operators (`+`, `-`, `*`, `/`) for custom data types to support arithmetic operations directly using Python syntax. This enhances the usability of the system and allows for expressive and clean code when performing operations between complex and rational numbers.

### 4. Implementing Coercion for Multiplication and Subtraction
- Expanded the system to automatically handle type coercion between complex and rational numbers during multiplication and subtraction, ensuring that operations yield correct results regardless of operand types.

### 5. Adding Support for Division
- Implemented support for division, completing the set of basic arithmetic operations. This involved handling complex division according to mathematical rules and ensuring that the division of rational numbers is correctly simplified.

### 6. Finalizing Operator Overloading and Division Support
- Finalized the arithmetic system by ensuring full support for operator overloading, including division, across all custom data types. This step involved refining the system to handle edge cases and improve the efficiency of operations.

## Conclusion
Lab 11 offers a comprehensive exploration into creating a flexible and powerful arithmetic system using generic functions and operator overloading in Python. Through these exercises, you've gained valuable insights into managing complex operations across different data types in a type-agnostic manner, showcasing the strength and versatility of Python's programming model.
