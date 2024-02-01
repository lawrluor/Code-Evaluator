balancing numbers = 6 is: 1+2+3+4+5 = 7+8

# user_num = 4
0123 4 567...

left_sum = 0 + 1 + 2 + 3 = 6

Is there any combination of numbers after 4 that can be added up to equal 6?

left_sum == right_sum
       6 == 5 + 6

if right_sum > left_sum:  # what comparison operator do we need to put here
    print("Not a balancing number")
