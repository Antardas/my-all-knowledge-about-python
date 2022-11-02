
import numbers


list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sum(list_of_numbers))


sets_of_numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# print(sum(sets_of_numbers))
total = 0
for i in sets_of_numbers:
    total += i

tuple_of_numbers = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

for i in tuple_of_numbers:
    print(i)


course = {
    'name': 'python',
    'code': 'PY',
    'duration': 3,
    'price': 1000

}

for key in course:
    print(key, course[key])

