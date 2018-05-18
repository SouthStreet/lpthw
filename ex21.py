def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + # BUG:

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - # BUG:

def multipy(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b

print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multipy(90, 2)
iq = divide(100, 2)


print(f"Age : {aage}, Height: {height}")
