def tell_my_name(name):
    print(f"My Name is {name}")
    return name + " Das"


full_name = tell_my_name("Antar")

print("My Full Name is ", full_name)

# Default Parameter


def multiply(num1, num2=10):
    return num1 * num2


sum = multiply(5)

print(sum)


def gusti_name(self, *gusti, **por_gusti):
    print(self)
    print(gusti)
    print(por_gusti)


gusti_name("Antar Das", 'abir',  'Rahul', "Pritom",
           shoshur='dulal', shshuri='kanta')
