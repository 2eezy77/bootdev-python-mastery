def in_inventory(recipe, inventory):
  correct = 0
  required_yet_not_acquired = []

  for ingredient in recipe:
    if ingredient in inventory:
      correct += 1
    else:
      required_yet_not_acquired.append(ingredient)
  
  correct_percentage = correct / len(recipe) * 100
  return correct_percentage, required_yet_not_acquired

def test():
  mac_and_cheese = [
    "pasta",
    "cheddar cheese",
    "black pepper",
    "salt",
    "love"
  ]
  pantry = [
    "pasta",
    "salt",
    "love" 
  ]

  perc, missing_pieces = in_inventory(mac_and_cheese, pantry)
  print(perc, missing_pieces)

def main():
  test()

main()
