# Lists

- List of items
- Declared using square brackets with commas separating items; accepts any data-type 
- Started using it by storing a list of strings.

# Acceptable List Readability (Preferance-based design) 

- Can structure in a column format
- Used when there are many items in a list and reading becomes hard
- No specific format other then regular syntax requirements.

# Acceptable Data-types

- All of them

# Counting list items

- Computers count the first item as 0; that's how we count items in lists.

# Indexing list items

- Similar to function calls: calling function, function runs and stores result, then returns result to caller and printed when printing happens.
- syntax: dictionary = [0,1,2,3,4, index_second_item = 1, print(dicitonary[index_second_item)

# Indexing list items from variable

- Initialize a list by storing it within a variable then print that variable with the correct syntax for calling a specific item, e.g., print(variable_list[index#)

# Retrieving list length

- Use len() function e.g., print(len(variable_list))
- Notice a pattern? The storing of a list is required, but watch out, you can't subscript a function; attempting to retrieve any information from a function directly, you have to store that information within a variable and then use that variable accordingly.
- expect total_len - 1; computer counts item 1 as 0 and so on...

# List Index updates

- Updating list indexes
- syntax: list_variable[index = "updated index"
- Try, if list_variable[index == "unwanted index": list_variable[index = "update to this"

# append() function

- Adds item to the of list e.g., list.append("item you want to append")
- Typically, lists are created with no values and designers will append values using loops. 
- For example, you can store the len of total_users individually to a list using a for loops range(), appending the iterations of i from 0 to the total_users into an empty list and it will store the incrementation of the user count into the empty list.

# pop() function

- removes the last item in the list[ and stores it for later use within a variable.
- Can pop specific list[items by using variable = list.pop(item); not restricted to just popping last item.
- syntax: popped_item = list.pop(option_item)

# checking list for certain items

- use a loop to increment over list[items to check whether it has certain values and returning the count of those specific items; make sure you initialize the variable_count(s) within the function you run the loop.
- use for loop in range(0, len(list)), check if each list[i incrementation "is equal to" what you are looking for and increment the counter of the corresponding variable that matches the item you matched.
- great full checking whether lists contain certain values and keeping track of how many times they come up within that list.

# No-Indexing over item's in a list

- If you don't need the index number then using the no-indexing syntax is the most efficient and easiest to read; 'for item in items:' declares the variable item using the in keyword.
- in comparison to 'for i in range(0, len(list)):', which is harder to reader.

# Find an Item in a list

- Using the no-indexing, one can accomplish with ease, being that iterating through each item now reads easier.
- 

# Comparing two lists using len() range loop and comparison operators with list[i incrementation. [13_find_increase.py] & [_find_increase_again.py]
- Useful when comparing old player levels with new player levels and seeing which list items have changed.

# Find Max "So Far" Using float("-inf") [14_find_max.py]
- Set negative infinity as you would a counter to keep track of incoming integers.
- Loop using no-indexing to compare iterations of the argument inputs to the negative infinity variable; include test for empty, where if empty, returns negative infinity.
- Meant to iterate over all items of a list and print the highest number.

# Finding odd numbers in list using index loop and modulus and extracting them using .append(i to new list. [15_get_all_odds.py]
- Loop using indexes (i in range(0, num and if some iteration's remainder, if divided by 2, is not 0 then append that to a list of odd_numbers[; otherwise continue to next iteration.
- 

# Slicing a list of team names using the : operator
- Just like the range( function it allows us to start, end, and step around the list. We can also ommit the use of any slicing options and only use what we need.
- Input a list of team names and use the list slicing operator to return 3 new lists. You can return the operation and the return will create the new lists. 

