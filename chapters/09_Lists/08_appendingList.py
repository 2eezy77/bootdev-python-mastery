empty_list = []

def appending_list(total_num):
    for i in range(0, total_num):
        empty_list.append(i)
    return empty_list


def main():
    num_users = 99
    store_len_users = appending_list(num_users)
    print(store_len_users)

main()
