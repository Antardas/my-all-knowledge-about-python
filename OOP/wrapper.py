def make_anything(a, b, bc):
    print('I am making anything')
    bc(a, b)
    print("I am calling the callback")


def cb():
    print('You called me!')


def sum(a, b):
    print(f'sum = {a + b}')


make_anything(1, 5, sum)
