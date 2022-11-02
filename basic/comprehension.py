numbers = [1, 5, 6, 9, 8, 5, 23, 6, 5, 47]

odd_numbers = []
for number in numbers:
    if (number % 2 == 1):
        odd_numbers.append(number)

# print(odd_numbers)

# simple comprehension

odd_numbers2 = [num for num in numbers if num % 2 == 1]

print(odd_numbers2)
