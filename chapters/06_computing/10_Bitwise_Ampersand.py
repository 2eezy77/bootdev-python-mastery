can_read = 0b1000
can_write = 0b0100
can_execute = 0b0010

def test_can_read(user_permission):
    test_permission = user_permission & can_read
    return test_permission

def test_can_write(user_permission):
    test_permission = user_permission & can_write
    return test_permission

def test_can_execute(user_permission):
    test_permission = user_permission & can_execute
    return test_permission

'''Check if user permissions are equal to the requirements'''
def main():
    user_permission = 0b1111
    can_i_r = test_can_read(user_permission)
    can_i_w = test_can_write(user_permission)
    can_i_x = test_can_execute(user_permission)

    print(can_i_r)
    print(can_i_w)
    print(can_i_x)

main()
