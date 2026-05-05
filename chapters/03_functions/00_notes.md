# Functions

* Helps make code less tedious by helping reuse code that we'd have to rewrite.
* by creating a function, e.g., math equation they'd otherwise have to rewrite for each time they needed it all they now have to do is call their new function and continue with whatever else they had to do.
* like creating a robot that opens the door for you, as long as someone rings the doorbell and you accept their entry.

# Functions review

* Functions are efficient if you need to use the same code over&over again.
* parameters are the acceptable inputs when calling the function
* must store the function in a variable when calling; like how we reuse, recycled goods, otherwise what's the point; that new variable stores the returned value of the function call.

# Using variables with Functions

* variables can be used to pass data into a function, as long as one keeps track of the valid parameters, and follows the structure.
* useful with python because it allows dynamic typing

# Multiple Parameters

* Functions can make as many parameters as possible.
* Callers match parameter order with argument.

# Printing v. Returning

* Print() is a function that prints to the console.
* Return is a keyword that causes the function's codeblock to end and returning stored values (pun intended) back to calling variable.
* print() is best used for debugging to ensure intended output; DO NOT PUSH CODE THAT CONTAINS PRINT(), that's personal use only.

# Where to define functions

* Code runs top to bottom, remember this!
* Calling a function or variable requires that the variable or function is first defined.
* you will get a "variable not defined" error.

# Order of functions

* Functions are normally defined at the top with the "entrypoint" main() function called first after all the functions have been defined.

# Understanding functions

* A parameter, if required, is the required input to allow for a valid function response.
* A function's body is where the instruction lies if the function is called; otherwise the function is a sleeper agent.
* "return" is the keyword that stores the data that is intended to be returned; ending the computer instruction once return is hit.

# Number of time's function is called?

* Typically, function calls are stored in it's own variable to ensure the resulting data is stored properly.
* Clean code ensures function calls are identified properly with each result easily retrievable for later use (Variable).

# Creating your own test() function to ensure code functionality

* Core concept = How to test function instruction to ensure functionality.
* test() controls the function call and establishes a framework for testing your own code within the same file.
* call the function you are testing within test() and print result using the variable of the called function you are testing.

# Functions that return None

* different ways that functions might end up returning None and why it's sometimes useful
* Returning None controls what the function returns to caller.
* Would use if wanting to use print but ensure return still works without returning a value.

# Multiple return values & receiving multiple values

* Functions are allowed to return multiple values and callers are able to receive multiple values as long as they both separate the values with commas.
* When assigning multiple receiving values, the variables are assigned the values in the same order received.
* Use identifiable names for the variables to ensure clean code.

# Parameters v. Arguments

* Parameters are the inputs expected to be supplied by the caller
* Arguments are the actual inputs supplied in place of the parameters by the caller.
* Parameters are empty space to illustrate what values are required to run the function & arguments are the values used in the function when ran.

# Default parameter values

* In-case the caller doesn't provide a value, it can keep the function from failing.
* Best controls optional function parameters; comes after all required parameters.
* Used in anticipation of caller not providing parameter value.

# How to complete a function requesting one argument and returning two values

* Read the question to ensure you understand the structure that it is requesting; here it's requesting to complete a function (defining, setting parameters, code block, returning correct values)
* Don't begin to code unless you understand the core concept and what it's requesting.
* One parameter doesn't restrict how much you can return it's just asking for a key to get the door open and retrieve items.

# function with 3 parameters but only returning two values

* doesn't matter, parameters are inputs requested from the function to complete instructions
* returning values are the values returned to caller after the function's code block runs.
* Two separate instructions inside "functions". parameters are like the passcode requests, return values are the items after gettting passed the passcode lock.
