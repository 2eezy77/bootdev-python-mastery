'''Converting hours to seconds'''
def hours_to_seconds(hours):
    to_sec = hours * 3600
    return to_sec


'''Using functions to test other functions'''
def test(hours):
    sec = hours_to_seconds(hours) # Notice how we stored the result of the data value to later implement in our test; the print() is our true test. 
    print(f"{hours} hour in seconds is {sec}")

'''Calling test where the true functionality is tested is stored'''
test(1)
test(10)
test(30)