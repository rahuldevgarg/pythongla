import random

# shuffle
L = [1, 2, 3, 4, 5]
random.shuffle(L)
print(L)

# random
re = random.random()
print(re)

# randrange
re = random.randrange(0, 10, 9)
print(re)

# randint
re = random.randint(0, 10)
print(re)

# choice
L = ['Divya', 'rahul', 'Vanshi', 'ashutosh']
re = random.choice(L)
print(re)

# choices
L = ['Divya', 'rahul', 'Vanshi', 'ashutosh']
re = random.choices(L, k=10, weights=[10, 60, 3, 5])
print(re)

# uniform
re = random.uniform(2.4, 2.5)
print(re)
