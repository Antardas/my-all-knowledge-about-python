print("My Function Run")
def sumAllNumber(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum