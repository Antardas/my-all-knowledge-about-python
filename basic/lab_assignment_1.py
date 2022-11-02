

# def create_string():
#     l = ["This", "is", "very", "fantastic"]

#     for i in l:
#         print(i, end=" ")

# create_string()

# def print_hi():
#     return "hi"


# print(print_hi())

# import requests


# res = requests.get(
#     "https://api.openweathermap.org/data/3.0/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=aaa02c5212f53ff280e5d227c0b503ea")
# print(res.json())

# import pyjokes
# def tell_some_jokes():
#     print(pyjokes.get_joke())

# tell_some_jokes()

""" def clean_string(s):
    ans = ""
    for c in s:
        if (ord(c) >= 65 and ord(c) <= 90):
            ans += c
        elif (ord(c) >= 97 and ord(c) <= 122):
            ans += c
    return ans


s = "P::::::,,,,,h;;;;i,,,t--r;,:o..N"
output = clean_string(s)
print(output) """

# Ans 7

"""
def replace_comma_with_space(text):
    final = ''
    for c in text:
        if c == ',':
            final += ' '
        else:
            final += c
    return final


s = "I,have,been,practising,python,since,the,course,started"

output = replace_comma_with_space(s)
print(output)
 """
"""

def make_upper(text):
    return text.upper()


def make_capital(text):
    return text.capitalize()

def make_lower(text):
    return text.lower()


def test_script(text):
    print(make_upper(text))
    print(make_capital(text))
    print(make_lower(text))

s = "I have been practising python since the course started"


test_script(s) """


# Ans 9

"""
# 5
def create_list():
    x = {'!': 1, '@': 2, '#': 3, '$': 4, '%': 5, '^': 6}
# output = [ 'a', 1, 'b',  2, 'c', 3, 'd', 4]


    output = []

    for key, value in x.items():
        output.append(key)
        output.append(value)

    print(output)

create_list() """

# Ans 9


# if words have in replace_with then replace with the next word in the list
"""

def replace_word():
    replace_with = ["chief", "thief", "superintendent",
                    "sweeper", "married", "left", "tried", "died"]

    s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

    s.replace("a", "brother")

    words = s.split(" ")
    for i in range(len(words)):
        if words[i] in replace_with:
            words[i] = replace_with[replace_with.index(words[i]) + 1]

    print(" ".join(words))


replace_word() """


# Ans 10

def create_new_string():
    a = ['oh', 'Emelia', 'to']
    new_a = list(map(str.lower, a))

    s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

    words = s.split(" ")

    new_string = ""
    f = open("out.txt", "a")
    
    for i in range(len(words)):
        low = words[i].lower()
        low = (low.replace(",", ""))
        low = (low.replace(".", ""))
        if low in new_a:
            new_string += words[i+1] + " "

    f.write(new_string)
    f.close()


create_new_string()
