# Lab 4: Environment Models and Recursion in Python

## Overview
In Lab 4, we explore the intricacies of environment models and recursion within Python, aiming to understand how Python manages variable scopes, namespaces, and how functions interact with these scopes. This lab is crucial for grasping the underlying mechanisms that support Python's execution model and for mastering recursion, a powerful tool in algorithmic problem solving.

## Objectives
- Illustrate Python's environment model through various code examples.
- Understand variable scope, including local, non-local, and global scopes.
- Master recursion with a practical example of a factorial function.

## Exercises Overview and Solutions

### Environment Models
The exercises require drawing the environment model for given Python scripts to understand variable scopes and how functions access and modify these variables.

1. **Variable Modification within a Function**:
   - Demonstrates local and global variable interaction and potential errors when trying to modify a global variable locally without explicit declaration.

2. **Nested Functions and Variable Updates**:
   - Explores how nested functions can access and modify variables in their enclosing scope.

3. **Usage of `nonlocal` and `global` Keywords**:
   - Differentiates between `nonlocal` and `global` keywords to manage variable scope effectively.

### Practical Recursion Application
- **Factorial Function**: Provides a classical example of recursion by implementing a factorial function.

## Solution Strategy
For each of the environment model exercises, the approach is to manually trace the code execution and visualize how Python creates and modifies environments and variable bindings. Since the solutions are visual, diagrams were created to represent each step of execution, showcasing how variables are scoped and accessed within different parts of the code.

### Tools Used for Visual Representation
- **Diagrams**: Used to illustrate environment models, variable scopes, and function calls. Each diagram represents the state of the environment stack at key points in the code execution.
- **Annotations**: Each diagram is accompanied by annotations explaining the changes in the environment and the rules that govern these changes, such as the creation of a new frame for function execution or the update of variable values within a specific scope.

### Recursion Explanation
- **Factorial Function Analysis**: A step-by-step breakdown of the recursive calls made by the factorial function, illustrating the call stack and the unwinding process as the base case is reached and the function returns values back up the stack.

## Conclusion
This lab emphasizes the importance of understanding Python's execution model and the power of recursion in programming. The ability to visualize environment models is crucial for debugging and writing efficient Python code. The recursive programming examples further solidify the concept of recursion as an elegant solution to certain types of problems.
