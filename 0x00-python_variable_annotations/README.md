
# Type Annotations and Static Typing in Python 3

## Introduction
Welcome to the **Type Annotations and Static Typing in Python 3** project! This repository aims to provide an in-depth understanding of type annotations, how they can be used to specify function signatures and variable types, the concept of duck typing, and how to validate your code using `mypy`.

## Type Annotations in Python 3
Type annotations in Python allow you to explicitly specify the types of variables, function parameters, and return values. They improve code readability and provide better documentation, helping developers understand what types of values are expected and returned.

**Example:**

def add(x: int, y: int) -> int:
    return x + y


## How to Use Type Annotations to Specify Function Signatures and Variable Types
### Function Signatures
You can specify the expected types for function parameters and the return type using type annotations.

**Example:**

def greet(name: str) -> str:
    return f"Hello, {name}!"


### Variable Types
Type annotations can also be used to specify the types of variables, providing clarity on the expected type of values.

**Example:**

age: int = 30
height: float = 5.9
name: str = "Alice"
is_student: bool = True


### Complex Types
You can use type annotations for complex types like lists, dictionaries, and tuples by importing them from the `typing` module.

**Example:**

from typing import List, Dict, Tuple

numbers: List[int] = [1, 2, 3, 4]
user_data: Dict[str, str] = {"name": "Alice", "email": "alice@example.com"}
coordinates: Tuple[int, int] = (10, 20)


## Duck Typing
Duck typing is a concept in dynamic typing where the suitability of an object is determined by the presence of certain methods and properties, rather than the actual type of the object. In other words, "if it looks like a duck and quacks like a duck, it must be a duck."

**Example:**

class Duck:
    def quack(self):
        return "Quack!"

class Dog:
    def quack(self):
        return "Woof!"

def make_it_quack(animal):
    print(animal.quack())

duck = Duck()
dog = Dog()

make_it_quack(duck)  # Outputs: Quack!
make_it_quack(dog)   # Outputs: Woof!


## How to Validate Your Code with `mypy`
`mypy` is a static type checker for Python. It checks the type annotations in your code and ensures they are being used correctly, catching potential type errors before runtime.

### Installation
To install `mypy`, use the following command:

pip install mypy


### Running `mypy`
You can run `mypy` on your Python files to check for type errors.

mypy your_script.py


### Example Usage
Here's an example of how to use `mypy` to check a file:
1. Create a Python file, `example.py`:
   
   def add(x: int, y: int) -> int:
       return x + y

   result = add(5, "10")  # This will cause a type error
   

2. Run `mypy` on the file:
   
   mypy example.py
   

3. `mypy` output:
   
   example.py:4: error: Argument 2 to "add" has incompatible type "str"; expected "int"
   Found 1 error in 1 file (checked 1 source file)
   

## Conclusion
This project covers the essentials of using type annotations in Python 3, specifying function signatures and variable types, understanding duck typing, and validating code with `mypy`. These tools and techniques enhance code readability, maintainability, and reliability. Explore the examples and documentation to deepen your understanding of these concepts.

