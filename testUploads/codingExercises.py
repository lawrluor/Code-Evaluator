# CodingBat
def sum13(nums):
  result = 0

  # i==0 is a special case: It is the first number, so there are no previous numbers to consider yet
  # Therefore, handle i=0 outside of the for loop, because we only need to do this once
  if len(nums) == 0:
    return result
  elif nums[0] != 13:
    result += nums[0]

  for i in range(1, len(nums)):
    if nums[i] != 13 and nums[i-1] != 13:
      result += nums[i]
    # print(i)
  return result

print(sum13([1, 2, 2, 1, 13]))
print(sum13([]))


#
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    # This is the simple level 1, with repetition, but fastest solution:
    def addCar(self, carType: int) -> bool:
        if carType == 1:
            if self.big > 0:
                self.big -= 1
                return True
            else:
                return False
        elif carType == 2:
            if self.medium > 0:
                self.medium -= 1
                return True
            else:
                return False
        else:
            if self.small > 0:
                self.small -= 1
                return True
            else:
                return False

    # More Sophisticated Solutions
    """
    # This solution fails because the size[carType] -= 1 is not referencing the actual variable
    # but just changing a number
    def addCarx(self, carType: int) -> bool:
        size = [None, self.big, self.medium, self.small] # [None, 1, 1, 0]
        if size[carType] > 0:
            size[carType] -= 1
            return True
        else:
            return False

    # This solution fails because we're not allowed to access string objects off of "self"
    def addCar(self, carType: int) -> bool:
        size = [None, "big", "medium", "small"]
        if self.size[carType] > 0: # self."big", self."medium"
            self.size[carType] -= 1
            return True
        else:
            return False
    """

    # Best solution: We can access objects and "chain" them through dictionaries
    # Slightly slower, however
    """
    def __init__(self, big: int, medium: int, small: int):
        self.available_sizes = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        if self.available_sizes[carType] > 0:
            self.available_sizes[carType] -= 1
            return True
        return False
    """



# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)


# Convert all 0s to 1s in a string without using loops
# https://www.w3schools.com/python/python_ref_string.asp
# http://www.asciitable.com/
def switchBits():
  translate_dict = {48: 49, 49: 48}

  print(original)
  return original.translate(translate_dict) # Also look up .maketrans() which is a string method that creates a mapping table

print(switchBits("011010101010"))
