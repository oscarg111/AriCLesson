import numpy as np

"""

Numpy

    - Library used to work with arrays
    - short for Numerical Python
    - To get numpy, 'import numpy as np'

"""

grades = [92, 93, 94, 99, 87]
grades_np = np.array([92, 93, 94, 99, 87])

print(type(grades_np))
print(grades_np // 2)
print()
print(type(grades))
print(grades)

zero_d = np.array(5)
print(zero_d)
print(zero_d.ndim)
print(grades_np.ndim)

two_dim = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
print(two_dim.ndim)
print(two_dim)

three_dim = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])
print(three_dim.ndim)
print(three_dim)

print(grades_np[0])
print(two_dim[1][1])
print(three_dim[1, 0, 2])

"""
Print out all of the elements in a 2D Array
___________________________________________
- Access the indexes and print each item at each index
    - Need to know the width and height of the 2D array
"""
print(len("Oscar"))
print(len([1, 2, 3, 4, 5]))
print(len(two_dim))

for item in grades:
    """print out the zero dimensional arrays in grades"""
    pass

for one_d in two_dim:
    for zerod in one_d:
        print(zerod, end=" ")
    print()
for twod in three_dim:
    """How can we print out all of the elements in the three dimensional array"""
    print("-------------------")
    for oned in twod:
        for zerod in oned:
            print(zerod, end=" ")
        print()
"""
zero_d
grades[0]
two_dim[1, 0]
three_dim[1, 0, 1]
"""

"""
Make a function that takes in a three dimensional array
- inside the function, go through the elements in the array.
- if the element is even, print the element.
- if the element is odd, do not print the element.

three_dim = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]])

To check if a number is even:

if num % 2 == 0:
    num is even
else:
    num is odd
"""
"""
Make a program that asks the user what indexes they would like to change, and the new
element, and replace the element at the index with the new element
"""
print("Here is the array:")
print(three_dim)

# first_ind = int(input("What 2nd dim array do you want?\n")) - 1
# sec_ind = int(input("What 1st dim array do you want?\n")) - 1
# third_ind = int(input("what value do you want\n")) - 1
#
# print(three_dim[first_ind, sec_ind, third_ind])

x = np.where(grades_np % 2 == 0)
print(x)

y = np.where(three_dim == 15)
print(y)

arr1 = np.array([1, 3, 5, 7, 9])

print(np.searchsorted(arr1, 4))
print(np.searchsorted(arr1, [2, 4, 6]))

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
"""
make a function that returns the index of the location where a passed in integer
would fit inside of the array, then I want you to print the new array


"""


def find_sorted(arr, num):
    index = np.searchsorted(arr, num)
    print(f"Your index is {index}")
    print("[", end=" ")
    for ind, val in enumerate(arr):
        if ind == index:
            print(num, end=" ")
        print(val, end=" ")
    if num >= arr[len(arr) - 1]:
        print(num, end=" ")
    print("]", end="")


find_sorted(arr2, -2)
print()
names = np.array(["Oscar", "Ari", "Eli"])
print(np.sort(names))

bools = np.array([True, False, True, True, False])
print(np.sort(bools))

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

nums = np.array([1, 2, 3, 4, 5, 6, 7, 8])
filter_arr = nums % 3 == 0

print(filter_arr)
print(nums[filter_arr])

"""
Function that filters the values and only prints those that are
higher than a number
"""


def higher_num(np_arr: np.array, num) -> np.array:
    """
    1) Create an empty array
        - this will be the filter array that you populate with booleans
    2) Use a for loop to go through the values in the array
        - in the for loop, there will be an if statement.
            if element > num:
                filter_arr.append(True)
            else:
                filter_arr.append(False)
    3) Once the function finishes, we will return a new array np_arr[filter_arr]
    """
    filter_arr1 = []
    for element in np_arr:
        # if the element is higher than 42, set the value to True, otherwise False:
        if element > num:
            filter_arr1.append(True)
        else:
            filter_arr1.append(False)

    return np_arr[filter_arr1]


arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# print(higher_num(arr1, int(input())))

x = np.random.randint(100, size=5)

"""
We will run a simulation to test randomness
_______________________________________________
- We will use a while loop to make many different random samples.
- Each random sample will be of size 100 and will have values that can be random integers up to
  100
- We will run this experiment until we have collected 100 random samples
- in the while loop we will calculate the average of each sample
- we will average out these averages
"""

average_tot = 0
# for _ in range(100):
#     arr = np.random.randint(100, size=100)
#     average_tot += np.average(arr)

print(average_tot / 100)

two_d = np.random.randint(100, size=(4, 3, 4))
# 3 Dim: 4 two dim w 3 row and 4 column
print(two_d)

rand_floats = np.random.rand(5) * 10
print(rand_floats)

naruto_char = np.array(["Sasuke", "Itachi", "Madara", "Shusui", "Kakashi"])
print(np.random.choice(naruto_char))

arr = np.random.choice(naruto_char, size=(2, 3, 4))
print(arr)

arr = np.random.choice([1, 2, 3, 4, 5], p=[.2, .1, .6, .1, 0], size=100)
print(arr)

count_s = 0
count_i = 0
count_m = 0
count_sh = 0
count_k = 0
# for char in arr:
#     if char == "Sasuke":
#         count_s += 1
#     if char == "Itachi":
#         count_i += 1
#     if char == "Madara":
#         count_m += 1
#     if char == "Shusui":
#         count_sh += 1
#     if char == "Kakashi":
#         count_k += 1

print(count_s, count_i, count_m, count_sh, count_k)
#
# np.random.shuffle(naruto_char)
# print(naruto_char)

print(np.random.permutation(naruto_char))
print(naruto_char)

