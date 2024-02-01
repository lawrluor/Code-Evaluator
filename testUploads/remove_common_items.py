# Write a function definition named get_values_not_in_common that takes two lists and returns a single set with the values that each list does not have in common
# Write a function definition named get_values_not_in_common that takes two lists and returns a single set with the values that each list does not have in common
def get_values_not_in_common(li1, li2):
  nums = set(li1) # This will hold all the numbers we've currently seen
  removed_nums = []

  for y in li2:
    if y in nums:
    	nums.remove(y)
      # TODO: Store the number to remove, then remove at the end
    else:
      nums.add(y)
  print(nums)
	return nums

assert get_values_not_in_common([5, 1, 2, 3], [3, 4, 5, 5]) == {1, 2, 4}
assert get_values_not_in_common([1, 1], [2, 2, 3]) == {1, 2, 3}
assert get_values_not_in_common(["tomato", "mango", "kiwi"], ["eggplant", "tomato", "broccoli"]) == {"mango", "kiwi", "eggplant", "broccoli"}
print("Exercise 86 is correct.")



# EXAMPLES
x = "5" # strings are usually words, text
int(x) # converts this string "5" into an integer 5
# casting: change one (similar) data type in python to another



# Example set function usage
print(set("kiwi"))
set([1, 2, 2, 3, 3, 3, 4, 4, 4, 4]) # {1, 2, 3, 4}

list_one = [1,2,3,4]
list_two = [2,3,5]

one_not_two = set(list_one).difference(list_two)
# set([1, 4])

two_not_one = set(list_two).difference(list_one)
# set([5])

# This could also be written as:
one_not_two = set(list_one) - set(list_two)
print(one_not_two)
