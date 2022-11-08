"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

casper = turtle.Turtle()

# for c in ['red', 'green', 'blue', 'yellow']:
#     t.color(c)
#     t.forward(75)
#     t.left(90)
number = input("Enter a number:")
# Python stores the input from the user as a
# string. 
print("You just entered: " + number)
# We need number as an integer, so we will use
# the int function
v = int(number)
# When printing only strings can be concatenated
# That's why we convert v+1 to a string before
# printing
print("Your number plus one is:" + str(v+1))
# You can also do it in one line
print("Your number plus one is: " + str(int(number)+1)  )
# For loops
# Goal: is to count up to the number the user entered - 1
# starting from zero
for i in range(v): # i is the variable that will hold the count
  print(i)
# range(v) will make the loop count from 0 to v-1