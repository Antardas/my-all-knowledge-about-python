# string = "abba"

# def is_palindrome(string):
#     return string == string[::-1]

# print(is_palindrome(string))

# Write a program center_align.py to centre align all lines in the given file.

# def center_align(file_name):
#     with open(file_name, "r") as f:
#         lines = f.readlines()
#         max_len = max(len(line) for line in lines)
#         for line in lines:
#             print(line.center(max_len))

# center_align('H:\personal\Explore-language\Python\OOP\\file.txt')
# H:\personal\Explore-language\Python\OOP\file.txt

# def dash_reader(file_name):
#     with open(file_name, "r") as f:
#         lines = f.readlines()
#         for line in lines:
#             sub_lines = line.split("--")
#             for sub_line in sub_lines:
#                 print(sub_line.strip())
#                 print("[enter - read more, press q to quit]")
#                 if input() == "q":
#                     return
#                 else:
#                     continue

# dash_reader('H:\personal\Explore-language\Python\OOP\\file.txt')

# Ans 4
# def anagrams(list_of_string):
#     list_of_anagram = []
#     for i in range(len(list_of_string)):
#         # check if the string is already in the list

#         if list_of_string[i] in list_of_anagram:
#             continue
#         single_anagram = []
#         single_anagram.append(list_of_string[i])
#         for j in range(i + 1, len(list_of_string)):
#             if sorted(list_of_string[i]) == sorted(list_of_string[j]):
#                 single_anagram.append(list_of_string[j])
#                 list_of_string[j] = ''
#         list_of_string[i] = ''
#         list_of_anagram.append(single_anagram)
#     new_list = []
#     for i in range(len(list_of_anagram)):
#         if list_of_anagram[i][0] != '':
#             new_list.append(list_of_anagram[i])

#     return new_list

# print(anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node']))

# import keyboard

# def formateBook(Rawbook):
#     Final_book = {}
#     tempBook = Rawbook.split('--')
#     page_no = 1
#     for page in tempBook:
#         each_page = dict([(page_no, page)])
#         Final_book.update(each_page)
#         page_no += 1
#     return Final_book

# def getPage(book, pg_no):
#     if pg_no in book.keys():
#         return book[pg_no]
#     else:
#         return -1

# file1 = open('file.txt', 'r')
# Lines = file1.readlines()
# file1.close()
# book = Lines[0]
# book = formateBook(book)

# pg_no = 1
# print(getPage(book, pg_no))
# print('[enter - read more, press q to quit]')
# while True:
#     n = input('Enter a number to skip pages: ')
#     if n.isnumeric():
#         pg_no += int(n)
#         print(getPage(book, pg_no))
#         print('[enter - read more, press q to quit]')
#     else:
#         keyboard.read_key()
#         if keyboard.is_pressed('enter'):
#             pg_no += 1
#             print(getPage(book, pg_no))
#             print('[enter - read more, press q to quit]')
#         elif keyboard.is_pressed('q'):
#             break

def dash_reader(file_name):
    total_pages = 0
    with open(file_name, "r") as f:
        lines = f.readlines()
        for line in enumerate(lines):
            sub_lines = line[1].split("--")
            print(sub_lines)

            total_pages += len(sub_lines)
            print(sub_lines[0].strip())
            print("Total Pages", total_pages)
            print("[enter - read more or put a number, press q to quit]")
            n = input()
            if n == "q":
                break
            else:
                current_page = 0
                while (True):
                    previous_page = current_page
                    if current_page == total_pages - 1 and len(n) == 0:
                        break
                    else:
                        if (len(n) == 0):  # if enter is pressed
                            current_page += 1
                            print(sub_lines[current_page].strip())
                        else:
                            num = int(n)
                            if num < 0:
                                current_page = (current_page - abs(num))
                            else:
                                current_page = current_page + num
                            if current_page < 0:
                                current_page += 1
                            if current_page >= len(sub_lines):
                                previous_page +=1
                                current_page = previous_page
                            if (current_page == total_pages):
                                current_page = total_pages - 1
                            print(sub_lines[current_page].strip())
                        print(
                            "[enter - read more or put a number, press q to quit]"
                        )

                        n = input()
                        if n == "q":
                            break

dash_reader('H:\personal\Explore-language\Python\OOP\\file.txt')

# def nearly_equal(str1, str2):
#     count = 0
#     i = j = 0
#     while (i < len(str1) and j < len(str2)):
#         if (str1[i] != str2[j]):
#             count = count + 1
#             if (len(str1) > len(str2)):
#                 i = i + 1
#             elif (len(str1) == len(str2)):
#                 pass
#             else:
#                 i = i - 1
#         if (count > 1):
#             return False
#         i = i + 1
#         j = j + 1
#     if (count < 2):
#         return True

# print(nearly_equal("reset", "rest"))


# def dash_reader(file_name):
#     total_pages = 0
#     with open(file_name, "r") as f:
#         lines = f.readlines()
#         for line in enumerate(lines):
#             sub_lines = line[1].split("--")
#             print(sub_lines)

#             total_pages += len(sub_lines)
#             print(sub_lines[0].strip())
#             print("Total Pages", total_pages)
#             print("[enter - read more or put a number, press q to quit]")
#             n = input()
#             if n == "q":
#                 break
#             else:
#                 current_page = 0
#                 while (True):
#                     previous_page = current_page
#                     if current_page == total_pages - 1 and len(n) == 0:
#                         break
#                     else:
#                         if (len(n) == 0):  # if enter is pressed

#                             current_page += 1
#                             print(sub_lines[current_page].strip())
#                         else:
#                             num = int(n)
#                             if num < 0:
#                               break
#                             current_page = current_page + num
#                             if current_page < 0:
#                                 current_page += 1
#                             if current_page >= len(sub_lines):
#                                 previous_page += 1
#                                 current_page = previous_page
#                             if (current_page == total_pages):
#                                 current_page = total_pages - 1
#                             print(sub_lines[current_page].strip())
#                         print(
#                             "[enter - read more or put a number, press q to quit]"
#                         )

#                         n = input()
#                         if n == "q":
#                             break

# dash_reader('H:\personal\Explore-language\Python\OOP\\file.txt')


