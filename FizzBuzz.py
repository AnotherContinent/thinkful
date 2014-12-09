import sys

num_input = raw_input("Please enter a number: ")

try:
  num_input = int(num_input)
except ValueError:
  print("That is not a valid integer.")
else:
  for n in range(1,num_input):
    if n % 5 == 0 and n % 3 == 0:
      print("FizzBuzz")
    elif n % 5 == 0:
      print("Buzz")
    elif n % 3 == 0:
      print("Fizz")
    else:
      print(n)


        
