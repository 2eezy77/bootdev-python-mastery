# Loops
* Reusing code w/o rewriting tedious code.
* Definite integrals math formula controling the # of loops to run code.
* syntax is important, for i in rang(a,b): (inclusive of a, exlusive of b), then indent body of for-loop; that's the code that you want ran the # of times the loop runs. if you print i, it will print the range counter

# Loops Practice: for i in range(a, b): print(i)
* syntax is as follows: start with i = 0 (i - 1, current position when starting aka 0 not 1), if i is >= 10, exit loop, otherwise print i. add the next value to i (add 1 to i until), back to checking whenever i is >= 10, if so exit loop, otherwise print(i). Over and over again until i >= 10, if so, exit loop.
* Remember, whitespace is required syntax for for-loops; logically it makes sense because you want to re-use code, in a for-loop it reruns the loop and in each iteration of the loop it runs your code while quietly running iterations.

# for i in range(5, end):
* Translated step-by-step: 1. i = 5 (for i in rang(5)), 2. checks if i >= <end>, if it is then it exits the for-loop, otherwise it runs the body and go's back to step 1-2 where it increments the value i += 1; so i = 6 and re-checks if it's >= <end>, otherwise it runs the body and returns until it does then it exits.
* this rhetorically explains the need for the body to be indented. 

# Why would you want to use a loop? 
* To avoiding typing code you will reuse.
* helps type hundreds of iterations of an instruction that is typed once.

# for i in range(0, 1000): print(i)
* prints 0, 1, ... 999. Not 1000 because it is inclusive of 0 and exlusive of 1000
* only prints i as long as it is less than 1000. >= 1000 is the keyword that tells the computer to exit the loop.

# white-space requirement
* for-loop bodies require white-space, utilizing the traditional 4-space indentation minimum. 

# 3rd parameter in range(), The Step.
* The step allows you to control the number per iteration of i.
* If you added the step "2" it would count every other iteration.
* You can even go backwards with "-1" if you started at 3 and ended at 0, e.g. resulting in, 3,2,1.

# sum-of-numbers through a for-loop operation.
* Instead of 1+1+1+1 which we do when we run a for loop and print(i), we are now setting parameters to start and end and setting a variable "total" = 0 and using the parameters for our for loop range. Instead of printing(i), we use an in-place operator to increment the "total" variable by i which add's 1 after each iteration as long as i is below the expected range max, otherwise it exits the loop and we return teh total outside the loop.  

# sum-of-odd numbers through a for-loop operation
* Instead of 0+1+2+3+4 this is asking to retrieve the sum of ONLY ODD NUMBERS; so from 1 to 4 we are only using 1+3 and returning the total 
* Remember, if we were to count we are using the range function and if we only want odd numbers we must set it ourselves to be from 1 to some "ending" and ensure each iteration only loops on odd numbers so setting step to 2; Within each iteration "i" we increment "total" by "i" so each iteration adds itself until the loop is over and returning the total variable that stored all the results from the loop. 

# While loop
* a loop based on a conditional as long as it is true, otherwise it stops.
* can run forever if the conditional doesn't have an expected end, and that end can be reached. 

# Continue Statement
* Used to skip iterations, very useful if you want to shorten the number of computations your program has to do.
* counter vs no counter: counter is used to keep track of whether our conditional is True e.g., if counter < 3,
continue, otherwise reset the counter and print the iteration "i" in the for loop; make sure you are initializing the counter before the for loop and incrementing it within the for loop.
* no counter is for operations that dont require keeping track of the iteration number needed to manipulate. think, do we need to count each peanut we eat? if not, then disregard counter. 

# break statement
* unlike continue where it skips an iteration of a loop, break exits the loop entirely after the iteration. 
* typically used to cut loops short if a certain condition is met, otherwise it goes until the range(max) is met; e.g., after for n in range(42): if n * n > 150: break.
* Notice how there is no need for else: because the otherwise is rhetorical, just goes until it hits the max. If no range() is used and it's a while, it you would need an else: to exit because the while: would loop infinitely and return an error. At that point, break becomes unnecessary. 

# Match Countdown, countdown from 10 to 1. If 1, additionally "...Fight!".
* work backwords, use if-else statement. No need for break or continue.
* Trick problem, wants you to use break but break still prints 1... or every other number but 1, as ...Fight!. Wouldn't have known unless you tried.

# calculate players experience, xp acquired so far
* keep track of xp, set up a loop from 1 to current level where i is the counter.
* increment xp by i * 5 (level up is == level * 5); stored in xp.
* don't get tricked by using i as what you multiply by 5. i are all the levels up until your max level from 1 --> current_level which makes you add up all the equations of xp to get to each level == total_xp so far.

# Restore health using potions 1:1 ratio as long as health < max_health & num_potions > 0
* Use while loop to keep loop running as long as conditional is true.
* Add health while subtracting num_potions as long as while is true.
* return what is requested (health after regen and num_potions remaining)