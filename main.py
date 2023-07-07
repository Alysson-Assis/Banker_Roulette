import random
names = input("Give me everybody's names, separated by a comma. ").split(", ")
num_items = len(names)
print(f"{names[random.randint(0, num_items - 1)]} is going to buy the bill.")