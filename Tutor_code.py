# ==================================================
# PYTHON TUTOR -SHORT EXAMPLE, PYTHON COURSE EXAMPLE
# ==================================================

import datetime
import math
import random

# 1---------- INTRODUCTION ----------
def introduction():
    print("\n--- Introduction to Python ---")
    print("Definition")
    print("Python is a high-level, interpreted, general-purpose language.")
    print("It is widely used in data processing, calculations, automation, and AI.")
    print("\nExample:")
    print("print('Hello, Python')")


# 2---------- DATA TYPES ----------
def data_types():
    print("\n--- Data Types in Python ---")
    a = 10
    b = 3.5
    c = '"python"'
    d = "True,False"
    print("Integer:", a)
    print("Float:", b)
    print("String:", c)
    print("Boolean:", d)

# 3---------- OPERATORS ----------
def operators():
    print("\n--- Operators with Numbers ---")
    x = 15
    y = 4
    print("x =", x, "y =", y)
    print("Addition: x + y =", x + y)
    print("Subtraction: x - y =", x - y)
    print("Multiplication: x * y =", x * y)
    print("Division: x / y =", x / y)
    print("Floor division: x // y =", x // y)
    print("Modulo: x % y =", x % y)
    print("Exponent: x ** y =", x ** y)

# 4---------- IF ELSE ----------
def if_else_example():
    print("\n--- If Else Example ---")
    print("Definitions")
    print("IF: checks a condition, if it is True then IF block executes")
    print("ELIF: checks another condition if IF condition is False")
    print("ELSE: executes when all above conditions are False\n")

    num = int(input("Enter a number: "))

    if num > 50:
        print("Positive number")
    elif num < 50:
        print("Negative number")
    else:
        print("Zero")


# 5---------- LOOPS ----------
def loops_example():
    print("\n--- Loops Example ---")
    print("Definition")
    print("FOR LOOP: used when we know how many times a loop should run")
    print("It repeats a block of code for a fixed range of values\n")

    print("For loop: print numbers 1 to 9")
    for i in range(1, 10):
        print(i, end=" ")
    print("\n")
    print("Definition")
    print("WHILE LOOP: used when we do not know exact number of iterations")
    print("It runs until the given condition becomes False\n")

    print("While loop: print squares of numbers 1 to 9")
    i = 1
    while i <= 9:
        print(f"{i}^2 =", i**2)
        i += 1

    print("\nSum of first 9 numbers using loop:")
    total = 0
    for i in range(1, 10):
        total += i
    print("Sum =", total)


# 6---------- TRY EXCEPT ----------
def try_except_example():
    print("\n--- Try Except Example ---")

    print("Definition:")
    print("The try block contains code that may cause an error.")
    print("The except block is used to handle errors so the program does not crash.")
    print("If an error occurs in the try block, the except block is executed.\n")

    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Result of division:", a / b)
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except ValueError:
        print("Invalid input, enter numbers only.")


# 7---------- FUNCTIONS ----------
def add_numbers(a, b):
    # This function takes two numbers and returns their sum
    return a + b

def multiply_numbers(a, b):
    # This function takes two numbers and returns their product
    return a * b

def functions_example():
    print("\n--- Functions Example ---")

    # Step 1: Function definition explanation
    print("Definition:")
    print("A function is a block of code that performs a specific task.")
    print("It runs only when it is called and helps to reuse code.\n")

    # Step 2: Getting input from the user
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    # Step 3: Using functions with user input
    print("Sum:", add_numbers(x, y))
    print("Product:", multiply_numbers(x, y))

    def square(n):
        # This function returns the square of a number
        return n**2

    num = int(input("Enter a number: "))
    print("Square:", square(num))


# 8---------- STRING METHODS ----------
def string_methods():
    print("\n--- String Methods Example ---")

    # ---------- DEFINITION ----------
    print("Definition:")
    print("String methods are built-in functions in Python that allow you to perform operations on strings,such as changing case, finding length, and formatting text.\n")

    # ---------- USER INPUT ----------
    text = input("Enter a string: ")

    # ---------- USING STRING METHODS ----------
    print("Upper:", text.upper())
    print("Lower:", text.lower())
    print("Title:", text.title())
    print("Length:", len(text))


# 9---------- LIST ----------
def list_example():
    print("\n--- List Example ---")

    # ---------- DEFINITION ----------
    print("Definition:")
    print("A list is an ordered collection of items in Python. Lists can store multiple values,allow duplicates, and can be modified after creation (mutable).\n")

    # ---------- EXAMPLE ----------
    my_list = [2, 4, 6, 8, 10]
    print("List:", my_list)
    print("Sum:", sum(my_list))
    print("Max:", max(my_list))
    print("Min:", min(my_list))
    print("List comprehension:", [x*3 for x in my_list])


# 10---------- TUPLE ----------
def tuple_example():
    print("\n--- Tuple Example ---")

    # ---------- DEFINITION ----------
    print("Definition:")
    print("A tuple is an ordered collection of items in Python, similar to a list,")
    print("but it is immutable (cannot be changed after creation).\n")

    # ---------- EXAMPLE ----------
    my_tuple = (1, 3, 5, 7)
    print("Tuple:", my_tuple)
    print("Sum:", sum(my_tuple))
    a, b, c, d = my_tuple
    print("Unpacking:", a, b, c, d)


# 11---------- DICTIONARY ----------
def dict_example():
    print("\n--- Dictionary Example ---")

    # ---------- DEFINITION ----------
    print("Definition:")
    print("A dictionary is an unordered collection of key-value pairs in Python.Each key must be unique, and values can be accessed, modified, or deleted using keys.\n")

    # ---------- EXAMPLE ----------
    my_dict = {"Ali": 80, "Sara": 90, "Omar": 75}
    print("Dictionary:", my_dict)
    print("Names:", list(my_dict.keys()))
    print("Marks:", list(my_dict.values()))
    print("Total:", sum(my_dict.values()))
    print("Average:", sum(my_dict.values()) / len(my_dict))


# 12---------- OOP ----------
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name, "Marks:", self.marks)

class ScienceStudent(Student):
    def percentage(self, total_marks):
        return (self.marks / total_marks) * 100

def oop_example():
    print("\n--- OOP Example ---")

    # ---------- DEFINITION ----------
    print("Definition:")
    print("Object-Oriented Programming (OOP) in Python allows you to create classes and objects.A class is a blueprint for objects, and objects are instances of classes.OOP helps organize code, reuse it, and model real-world entities\n")

    # ---------- USER INPUT ----------
    name = input("Enter student name: ")
    obtained_marks = float(input("Enter obtained marks: "))
    total_marks = float(input("Enter total marks: "))

    # ---------- USING CLASSES ----------
    s = ScienceStudent(name, obtained_marks)
    s.display()
    print("Percentage:", round(s.percentage(total_marks), 2), "%")



# 13---------- DECORATORS ----------
def decorator_example():
    print("\n--- Decorators Example ---")

    # ---------- DEFINITION ----------
    print("Definition:")
    print("A decorator is a function that takes another function as input,")
    print("adds some functionality, and returns a new function.")
    print("Decorators are used to modify or enhance functions without changing their code.\n")

    # ---------- EXAMPLE ----------
    def deco(func):
        def wrapper():
            print("Before function")
            func()
            print("After function")
        return wrapper

    @deco
    def hello():
        print("Hello Python")

    hello()


# 14---------- FILE HANDLING ----------
def file_handling_example():
    print("\n--- File Handling Example ---")

    # ---------- DEFINITION ----------
    print("Definition:")
    print("File handling in Python allows you to create, read, write, and modify files.")
    print("Common operations include opening a file, reading/writing data, and closing the file.\n")

    # ---------- SIMULATED FILE CONTENT ----------
    numbers = [str(i) for i in range(1, 6)]
    print("Numbers 1 to 5:")
    for n in numbers:
        print(n)

    print("\n(Note: File writing is skipped in online compilers due to permission restrictions)")


# 15---------- CLASS AND INHERITANCE ----------
class Person:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def show_details(self):
        # Show inheritance relation manually
        print("Class: Teacher (Child) inherits from Person (Parent)")
        self.show_name()
        print("Subject:", self.subject)

def class_inheritance_example():
    print("\n--- Class and Inheritance Example ---")

    # ---------- DEFINITION ----------
    print("Definition:")
    print("Inheritance in Python allows a class (child) to inherit attributes and methods from another class (parent).It helps reuse code and model real-world relationships.\n")

    # ---------- USER INPUT ----------
    name = input("Enter teacher name: ")
    subject = input("Enter subject: ")

    # ---------- USING CLASSES ----------
    t = Teacher(name, subject)
    t.show_details()



# 16---------- QUIZ ----------
def save_result(name, score, total):
    print("\n--- Result ---")
    print("Name:", name)
    print("Score:", score, "/", total)


def quiz():
    print("\n--- Python Quiz ---")

    questions = {
        "1. What is the output of: print(5 + 3)? ": "8",
        "2. What is the output of: print(4 * 2)? ": "8",
        "3. What is the output of: print(20 / 4)? ": "5.0",
        "4. What keyword is used to define a function? ": "def",
        "5. Which collection type stores numbers in order? ": "list",
        "6. What operator is used for exponentiation? ": "**",
        "7. What is the sum of 2, 4, 6? ": "12",
        "8. What is the average of 3, 6, 9? ": "6.0",
        "9. Is Python a high-level language? ": "true",
        "10. What is the output of: print(3**2)? ": "9",
        "11. What is the output of: print(10 // 3)? ": "3",
        "12. What is the output of: print(10 % 3)? ": "1",
        "13. x=[1,2]; x.append(3); print(x) ": "[1, 2, 3]",
        "14. x=[1,2]; x=[3,4]; print(x) ": "[3, 4]",
        "15. Which keyword defines function? ": "def",
        "16. Which collection stores numbers in order? ": "list",
        "17. Sum of 2, 4, 6? ": "12"
    }

    score = 0
    name = input("Enter your name: ")

    for q, ans in questions.items():
        user_ans = input(q).strip().lower()
        if user_ans == ans.lower():
            score += 1

    print("\nFinal Score:", score, "/", len(questions))
    save_result(name, score, len(questions))


# ---------- MAIN MENU ----------
def main_menu():
    while True:
        print("\n=== PYTHON TUTOR ===")
        print("1. Introduction")
        print("2. Data Types")
        print("3. Operators")
        print("4. If Else")
        print("5. Loops")
        print("6. Try Except")
        print("7. Functions")
        print("8. String Methods")
        print("9. List")
        print("10. Tuple")
        print("11. Dictionary")
        print("12. OOP")
        print("13. Decorators")
        print("14. File Handling")
        print("15. Class & Inheritance")
        print("16. Quiz")
        print("17. Exit")

        choice = input("Select option (1-17): ")

        if choice == "1":
            introduction()
        elif choice == "2":
            data_types()
        elif choice == "3":
            operators()
        elif choice == "4":
            if_else_example()
        elif choice == "5":
            loops_example()
        elif choice == "6":
            try_except_example()
        elif choice == "7":
            functions_example()
        elif choice == "8":
            string_methods()
        elif choice == "9":
            list_example()
        elif choice == "10":
            tuple_example()
        elif choice == "11":
            dict_example()
        elif choice == "12":
            oop_example()
        elif choice == "13":
            decorator_example()
        elif choice == "14":
            file_handling_example()
        elif choice == "15":
            class_inheritance_example()
        elif choice == "16":
            quiz()
        elif choice == "17":
            print("Good bye! focus on your goals :)")
            break
        else:
            print("Invalid choice. Try again.")


# ---------- START ----------
main_menu()
