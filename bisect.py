import bisect

"""
The bisect_left() / bisect_right() method finds and returns the position at which 
an element can be inserted into a Python list while maintaining the sorted order of the Python list. 

If the list already has elements with the same value as the new element, 
the insertion point is to the left / right of first such element.
"""

# given sorted list of numbers
nums = [1,3,5,7,10,25,49,55]

# given elements to be inserted into the list
ele1 = 25
ele2 = 26
ele3 = 55

# get index where to insert the elements
idx1_left = bisect.bisect_left(nums, ele1)
idx2_left = bisect.bisect_left(nums, ele2)
idx3_left = bisect.bisect_left(nums, ele3)

idx1_right = bisect.bisect_right(nums, ele1)
idx2_right = bisect.bisect_right(nums, ele2)
idx3_right = bisect.bisect_right(nums, ele3)

# print the index
print(f"Bisect left: Insert element {ele1} at index {idx1_left} in nums list to maintain sorted order.")
print(f"Bisect left: Insert element {ele2} at index {idx2_left} in nums list to maintain sorted order.")
print(f"Bisect left: Insert element {ele3} at index {idx3_left} in nums list to maintain sorted order.")
print()
print(f"Bisect right: Insert element {ele1} at index {idx1_right} in nums list to maintain sorted order.")
print(f"Bisect right: Insert element {ele2} at index {idx2_right} in nums list to maintain sorted order.")
print(f"Bisect right: Insert element {ele3} at index {idx3_right} in nums list to maintain sorted order.")
