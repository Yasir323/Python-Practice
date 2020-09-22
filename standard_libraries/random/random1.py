import random, string

print(random.random())  # Random no. b/w 0 and 1
print(random.randint(1, 10))    # Random no. b/w 1 and 10
print(random.choice([1, 2, 3, 4]))
print(random.choices([1, 2, 3, 4], k=2))
print(random.choices("qwertyuiop", k=8))
# We can use the above statement to generate random password
print("".join(random.choices("qwertyuiop", k=8)))
# An even better way
print("".join(random.choices(string.ascii_letters + string.digits, k=8)))


# Shuffle an array
odds = [x for x in range(20) if x % 2 == 1]
random.shuffle(odds)
print(odds)
