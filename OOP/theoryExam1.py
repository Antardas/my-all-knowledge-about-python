# Ans 1

#  2 ^ 3 = 8
""" def exp(a, n):
    return a ** n

print(exp(2, 4)) """

# Write a python to read three floating numbers from the keyboard in a single line with ‘-’ (dash) in between and output their sum.

""" def sum():
    numbers = input("enter numbers: ")
    numbers = numbers.split("-")

    sum = 0
    for i in numbers:
        sum += float(i)
    print(f"sum is: {sum}")

sum() """

# Write a python program to read a string from the keyboard and output the string in reverse order.
""" def reverse():
    string = input("enter string: ")
    string = string.split()
    
    for i in string:
        print(i[::-1], end=" ")


reverse() """

# Write a python program for the requirement below. Notice the output must be in sorted order -
# Input: x3b4U5i2
# Output: bbbbiiUUUUUxxx


""" def showWord():
    s = input("Input  :")
    sList= list(s)
    wList = []
    # step of list loop
    for i in range(0, len(sList), 2):
        wList.append(sList[i] * int(sList[i+1]))
    # Sort the without avoiding case
    wList.sort(key=str.lower)
    print("Output :", "".join(wList))


showWord() """


#  rite a python program to read student_name and mark from keyboard and store the data in a text file with an unique student_id .

# generator function for number


""" import random


def save_in_file_student_data():
    student_name = input("enter student name: ")
    mark = input("enter mark: ")
    # random number generator
    student_id = random.randint(1000, 9999)
    with open("student.txt", "a") as f:
        f.write(f"Id: {student_id} -> {student_name} -> {mark}\n")

save_in_file_student_data() """


# def func(arg1, arg2, arg3=4, arg4=5):
#     print(arg1, arg2, arg3, arg4)

# func(3, 4, arg2=1)

# Write a Python class to get all possible unique subsets from a set of integers.
""" 
class Subsets:
    def __init__(self, s):
        self.s = s

    def subsets(self):
        return self.subsetsRecur([], sorted(self.s))

    def subsetsRecur(self, current, s):
        if s:
            return self.subsetsRecur(current, s[1:]) + self.subsetsRecur(current + [s[0]], s[1:])
        return [current]

print(Subsets([4, 5, 6]).subsets()) """

# Write a Python class to find a pair of elements (indices of the two numbers) from a given array whose sum equals a specific target number.
# output = 3 4

"""
class Pair:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
    def pair(self):
        for i in range(len(self.arr)):
            if(self.arr[i] + self.arr[i+1] == self.target):
                return i+1, i+2

pair = Pair([10, 20, 10, 40, 50, 60, 70], 50).pair()
print(pair[0], pair[1]) 
"""

#9. Write a class with two instance variables X, n . Add two methods sum() and pow() to get the sum of X+n and exponential/power of Xn .
""" 
class SumPow:
    def __init__(self, x, n):
        self.x = x
        self.n = n

    def sum(self):
        return self.x + self.n

    def pow(self):
        return self.x ** self.n

sum = SumPow(2, 3).sum()
pow = SumPow(2, 3).pow()

print(sum, pow) """

# Write a Python class named Distance constructed by two points (x1, y1), (x2, y2) and a method which will compute the distance between those points.

""""""
class Distance:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        return ((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2) ** 0.5

print(Distance(2, 3, 4, 5).distance())

class Person:
    def __init__(self, id):
        self.id = id

sam = Person(100)
sam.__dict__['age'] = 49

print (sam.age + len(sam.__dict__))