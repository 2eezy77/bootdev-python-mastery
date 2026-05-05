## Chapter 2 - Variables
# What is a variable
* Variables store values
* can store strings or integers
* use a continuious word separated by '_' that is consistent with what you are storing; first_name = "lane"

# Variables Vary?
* because you can change the value of an existing variable if you just assign it a new value.

# Math & Variables
* Using python's syntax for mathematical operators
* Uses PEMDAS logic to solve math problems.
* Variables can be used to store values and later called on in mathematical equations. 

# Negative numbers
* just add a -. 

# Comments
* Used to add comments to code
* '#' is used a single line
* """ is used for docstrings aka multi-line comments

# Variable names
* in python, variables are named using snake_case; words are lower case and separated by '_'
* python still accepts cameCase or PascalCase as shown. Please just use snake_case and keep the tradition going. 

# Variables have different data values
* data types are just ways to differentiate different values
* strings are surrounded in ""
* integers are numbers without decimals, floats have those. booleans are 0's or 1's, True/False; comparison values.

# F-strings and interpolating them
* used to make variables useful within print statements with strings.
* with an f-string, one can add a variable, f"{varaiable}", without having to update each print() statement to what their variable's value is.

# None Type value
* Used to keep a variable that you will use later empty for now.
* None != "None"; careful None is not the same as the string version although they look the same when shown on the console. *type* print(type(variable_w_None))
* can be used to store an input value. user = input() 

# Dynamic Typing, or maybe ignore this one
* In python, one can update the value type of a variable; best not too.
* It's better to just create a new variable, you will most likely run into problems.

# Concatenation
* adding two string variables together using the + operator.
* best to just interpolate variables using f-strings due to having to take into account the _ in variables prior to concatenating. 
* May be necessary but interpolation using f-strings wins in efficiency. 

# Multi-variable Declaration
* Saving space by declaring all your variables on the same line.
* To ensure that code is easy to read, multi-variable declaration should be related to one-another. 
* easy-to-read = clean code

# How to use AI to help you learn
* The Socratic method is the best because it helps you apply the recall method to retrieve what you already know. 
* Dont use it to give you the answer but to help uncover what you already know. 
* Consequences in cheating is that you never learn anything but get an empty reward (dopamine) that makes you want to keep doing it.

# Reviewing data types
* Use the `type` keyword within the `print()` function to print the data type that was used.
* If wrong data type was used, one can change how it's declared to ensure valid syntax.