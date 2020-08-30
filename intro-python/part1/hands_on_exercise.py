"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print("This varible is of the type ", type(pi), "and the value is ", pi)

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i > 50:
    print("'i' is greater than 50, it's current vlaue is ",i)
elif i < 50:
    print("'i' is less than 50, it's current vlaue is ", i) 
else:
    print("Something strange has happened. 'i' is exactly 50. Let's check....The value of 'i' is currently", i)



# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == "orange":
    print("You've picked a citrus fruit. It's an {}. ".format(picked_fruit))
elif picked_fruit == "strawberry":
    print("You've picked a berry. It's an {}. ".format(picked_fruit))
elif picked_fruit == "banana":
    print("You've picked a tropical fruit. It's an {}. ".format(picked_fruit))

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def myMultiply(a,b):
    myResult = a * b
    return(myResult)

# TODO: Now call the function a few times to calculate the following answers


print("12 x 96 =",myMultiply(12,96))

print("48 x 17 =",myMultiply(48,17))

print("196523 x 87323 =",myMultiply(196523,87323))
