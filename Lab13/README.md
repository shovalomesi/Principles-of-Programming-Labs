# Lab 13: Building an Interpreter for Mathematical Expressions

## Overview
Lab 13 challenges you to extend a basic calculator program, `calc.py`, to support not just arithmetic operations but also comparisons, rounding of numbers, and global variables. Through this lab, you'll gain insights into the workings of interpreters, how to process and evaluate expressions, and how to maintain state within a program.

## Objectives
- Enhance a simple calculator interpreter to support additional operations and features.
- Implement comparison operators (`eq`, `lt`, `gt`) to enable expression evaluations that go beyond arithmetic.
- Add functionality for rounding numbers to a specified number of decimal places.
- Introduce support for global variables, allowing the calculator to store and reuse values across different expressions.

## Exercises Overview and Solutions

### 1. Tracking Calculator Operations
- Investigated how the `calc.py` interpreter processes input expressions, including simple numbers, arithmetic operations like `add` and `mul`, and handling of invalid operations. This step involved following the code execution path and understanding the interpreter's evaluation strategy.

### 2. Implementing Comparison Operators
- Extended the calculator to include comparison operators (`eq`, `lt`, `gt`), which allow it to perform equality and inequality checks. This feature requires parsing the expressions to identify the operators and operands and then applying the appropriate Python comparison to produce a Boolean result.

### 3. Rounding Numbers
- Added support for rounding numbers to the calculator. This involved implementing a `round` function that takes a number and the desired number of decimal places as arguments, leveraging Python's built-in `round` function to perform the operation and return the result.

### 4. Supporting Global Variables
- Enhanced the calculator to support global variables, enabling users to assign values to named variables and then use those variables in subsequent calculations. This feature required modifications to the interpreter to recognize variable assignment syntax, store variable values in a global context, and retrieve those values when referenced in expressions.

## Conclusion
Lab 13 offers a comprehensive exploration into extending a simple calculator program to support a wider range of operations and features, turning it into a more sophisticated interpreter. Through this lab, you've developed a deeper understanding of expression parsing, evaluation strategies, and state management within interpreters. These skills are invaluable for anyone looking to build or work with programming languages or complex data processing systems.
