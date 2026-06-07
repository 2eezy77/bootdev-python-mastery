def list_in_reverse(some_list):
  reverse = []

  for i in range(len(some_list) -1, -1, -1):
    reverse.append(some_list[i])
  return reverse

def test():
  list = [
    "going", "you", "are", "where"
  ]
  wanting_list_in_reverse = list_in_reverse(list)
  print(wanting_list_in_reverse)

def main():
  test()

main() 