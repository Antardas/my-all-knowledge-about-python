# with open("message.txt", "a") as file_object:
#     file_object.write("I love programming. and append this line to the file.\n")
# display_person() function call

def display(**kwargs):
    for i in kwargs:
        print(i, end=" ")
