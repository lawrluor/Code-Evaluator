from math import *

print ("Welcome to the Fibonacci number calculator!")
print ("(*☻-☻*)")

n=eval(input("Please enter a natural number"))

previous_previous=0
previous=1
if n==1:
    print("0")
elif n==2:
    print("1")
else:
  for num in range(n-2):
      print("Current n:", num+3)
      print("previous_previous:", previous_previous)
      print("previous:",previous)
      print("\n")

      total = previous_previous + previous

      # Update the variables to prepare for the next loop.
      previous_previous = previous
      previous = total

  #if n==3:
      #total=(x+y)
      #print(total)
  #if n==4:
      #print(total)
      #total=total+y
  #if n==5:
      #print()
  #total=(n-2)+(n-1)
  print("The Fibonacci number of your number is",total)
