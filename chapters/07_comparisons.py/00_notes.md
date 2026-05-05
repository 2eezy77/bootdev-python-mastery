# Comparison Operators 
* Boolean logic = operations that require comparison operators to compare values; results in either True or False. 
* The operators = > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to), != (not equal to),  == (equals to).

# Comparison Operator evaluation
* Comparison operator evaluations will always result either True or False, nothing else. 
* Don't use unless you are testign the comparing the result of two value

# Practice comparison operators to gets used to only expecting True or False
* == results in True or false although many times you might want to use it as an assignment operator, it's only for boolean logic because it's a comparison operator.
* Best used for instances when you want to store whether a car is_smaller or is_larger; u get the point.

# If statements
* Syntax is - if <statement>:, then indent the block that you want ran if True; remember to return after the block of code is ran. You must return all lines that are expected to be outputted. 
* Used when you want to run code, only if what you set is true. 
* Gives guidelines on when to output certain code.

# If statement practice
* == is a comparative operator that returns either True or False

# If-Else
* checks the initial "If:", otherwise it runs If-Else: statements. Finally, if neither the initial if or elif then it runs "Else" and returns whichever is True.
* can't have elif or else w/o if; can have else w/o elif. 
* These conditional statements are called branches if:, elif:, else:.

# If-Else statemetn practice
* elif stil requires a condition, else doesn't because it's just assumed, if nothing else worked, it's else.
* else looks different in syntax, else:, no conditional
* remember, If-Else statements require conditionals, using = is not a conditional because that assigns a value to a variable; common mistake, use == conditional operator.

# Boolean Logic
* Testing whether values are True or False, where logical operators thrive, remember and, or where and requires both values to be True to return True. Or requires one value to be True to return True.
* Can return the boolean logic statement directly without it having to be stored; remember not to format with ':' at end if returning directly because that will return a syntax error.
* Remember, non-numbers are returned as True in python. 

# Sometimes it's best to apply reverse-sychology to prevent over-nesting branches.
* When testing multiple comparison's, it causes you to over-nest if attacking directly; read problem, analyze whether it will cause you to over-nest. If so, try converting comparison's to negative in the attempt to ensure readability.
* No need to apply "on_break == True" if testing a boolean value; it becomes redundant.
* Goal should be to solve and keep Readability. 

# Not using else statement when requiring an "otherwise" statement.
* Create a regular 'if' statement, and return that; if that if statement doesn't meet requirements then it returns the second return statement.
* Else: isn't necessarily required if you just return the if statements.

# Updating Boolean Values
* If changing compared boolean values, change the value then return values
* Return all together while explicity stating what each returned value is; Literally returning all 3.
* 