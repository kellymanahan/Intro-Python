# Write a function is_even that will return true if the passed in number is even.

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
def is_even(num): 
  if int(num) % 2 == 0:
    print("even")
  else:
    print("odd")

is_even(num)