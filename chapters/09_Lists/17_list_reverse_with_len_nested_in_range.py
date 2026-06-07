def reverse_order(some_list):
  reverse_list = []

  for i in range(len(some_list) -1, -1, -1):
    reverse_list.append(some_list[i])
  return reverse_list

def test():
  list = [
    "going", "you", "are", "where"
  ]

  wanting_list_reversed = reverse_order(list)
  print(wanting_list_reversed)

def main():
  test()

main()
