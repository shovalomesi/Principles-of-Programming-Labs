# Lab 6: Abstract Data Types in Python

## Overview
In Lab 6, we explore Abstract Data Types (ADTs) to manage complex numbers and recursive lists in Python. This approach highlights the power of abstraction in software development, allowing for more manageable, reusable, and modular code. By implementing ADTs, we encapsulate data and operations, showcasing a profound understanding of data structures and object-oriented programming.

## Objectives
- Implement ADTs for complex numbers using tuples and dispatch dictionaries.
- Demonstrate operations on complex numbers, including addition, absolute value calculation, and string representation.
- Construct and manipulate recursive lists through ADTs for data organization and manipulation.
- Apply functional programming concepts to create and reverse recursive lists efficiently.

## Exercises Overview and Solutions

### Complex Numbers ADT
1. **Implementation using Tuples**:
   - We created ADTs for complex numbers where each complex number is represented as a tuple. Operations include:
     - `add_complex`: Adds two complex numbers.
     - `abs_complex`: Calculates the absolute value of a complex number.
     - `str_complex`: Returns a string representation of a complex number.
   - Example:
     ```python
     c = make_complex(2, 3)
     print(str_complex(add_complex(c, c)))  # Output: '(4+6i)'
     ```

2. **Implementation using Dispatch Dictionaries**:
   - Re-implemented the complex numbers ADT using dispatch dictionaries, allowing for a more dynamic approach to accessing and executing functions associated with complex numbers.
   - Example:
     ```python
     c = make_complex(2, 3)
     print(str_complex(c))  # Output: '(2+3i)'
     ```

### Recursive Lists ADT
3. **Recursive Lists using Tuples**:
   - Implemented an ADT for recursive lists, utilizing tuples to represent the nested list structure. This ADT includes operations for creating a list, accessing the first element, and accessing the rest of the list.
   
4. **Recursive Lists using Dispatch**:
   - Similar to the complex numbers ADT, recursive lists were also implemented using dispatch dictionaries to provide a flexible approach to managing recursive lists.

### Practical Applications
- **Complex Number Operations**: Demonstrated practical applications of complex numbers ADT by performing various operations, such as addition and calculating the absolute value, to solve mathematical problems.

- **Recursive List Manipulation**: Showcased the manipulation of recursive lists, including creating a list, reversing it, and applying it to solve problems requiring nested data structures.

## Conclusion
This lab emphasizes the significance of abstracting data types and operations in software development, providing a foundation for efficient and effective problem-solving. By mastering ADTs, you gain the ability to design and implement complex data structures, enhancing your coding toolkit for future projects.
