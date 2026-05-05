# Python Numbers & Arithmetics
* like mathematics, numbers without decimals are considered integers (both positive and negatives)
* Numbers containing decimals are called floats
* Arithmetics is performed as you might expect with most results outputting integers. Division is the only one that outputs a float.

# Floor Division
* rounds the result down to the nearest integer. 
* Learning C i figured this is because floats take up twice as much memory space.

# Exponents
* Python has built-in exponent syntax e.g., 6 ** 2 = 36
* Sometimes, python docs might say 6^2 but use 6 ** 2 to ensure accurancy. 

# Changing in place
* Since code reads right to left, the variabel doesn't update until after the operation done.
* Although it isn't efficient, it's still valid and should be understood that one can perform operations on a variable and still store it within itself, successfully updating itself to a new value. 

# Adding/taking from variables (+=, -=, *=, /=)
* Python allows adding to or taking from variables values using the appropriate operator symbol, as long as you use the assignment operator in congruence. 
* Cant use return to perform the operation, it has to be done prior to return then you can return the final value.

# Scientific Notation & Readability
* Using e or E followed by the number of places to move the decimal allows for an easier way to write numbers that are too tedious to type.
* Using '_' in place of ',' to separate large numbers helps for readability. 
* must use a float, because of the decimal place to use scientific notation.

# Logical operators and nesting logical operations
* logical operators deal with boolean values, where 'and' requires both operators to be True == True, 
and atleast 1 True for an 'or' operator == True
* logical operations can be nested, with same order of operations as typical arithmetic operations where the nested problem solved first then that value goes against the outer operator.

# Not (Stil a logical operator)
* Reverses the result of the boolean operation
* syntax is unique, 'not' should come before what you are reversing e.g., opposite = not a (if input true then false is the output)

# Binary to integer
* binary numbers are no different then regular decimals, just a greater multiple version of 2 in comparison to 10.
* syntax for converting binary to integer is with a leading 0b followed by the binary number you want to convert e.g, 0b0101 = 5

# Bitwise operations using Amperands '&'
* runs logical operations in a column-like format against each individual 0 & 1, where 1's are True & 0's False.
* Amperand is the Bitwise symbol '&' which is the comparison operator 'And' requiring both boolean values to be True to return True, otherwise False.
* Great for running comparison tests in a truncated format, to test whether a value compares true to what you compare it too e.g., can_edit = 0b0100 to user_permission = 0b0000 which results in a binary value of 0000 which returns False; Remember you have to establish the 0b prefix to all binaries you are using otherwise it will return an integer.

# Bitwise '|' (or) operator
* the | operator combines all logical operations where atleast 1 is present. 
* Like ampersand's '&', this '|' (or) operator compares bitwise operations using a column-like format comparing each digit to their corresponding.
* Used to output True, where atleast, one digit is a binary: 1 ('True' in the eyes of a bitwise); great for adding missing permissions to where they should be, as long as they are partners.

# Delimiter _ for integers
* Used for separating large numbers with _ for readability; can't use ','.
* Makes millions easier to read due to the 0's being spaced properly. 
* Small things that makes code easier to read.

# Converting Binary
* Using int() which takes a second argument to specify which base #, e.g., int('0101', 2) = 5 
* useful for when you want to output the string-version of a binary number. 
* Remember this is for converting BINARY-STRINGS (string data type 'text')  binary-literal (integer-literal 'number') two completely different data-types where integers can be used for mathematical and comparison (bitwise) where text is for visual representation.
