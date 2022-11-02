#1
# class Star_Cinema:
#     hall_list = []

#     def entry_hall(self, obj):
#         self.hall_list.append(obj)

# 2


# class Hall(Star_Cinema):

#     def __init__(self, rows, cols, hall_no):
#         self.seats = {}
#         self.show_list = []
#         self.rows = rows
#         self.cols = cols
#         self.hall_no = hall_no
#         super().entry_hall(self)


# Make a method in Hall class named entry_show() which will take id, movie_name and time in string format. Make a tuple with all of the information and append it to the show_list attribute. Allocate seats with rows and cols using 2d list, initially all seats will be free. Make a key with id to the attribute seats and value will be the 2d list.

# class entry_show():
#     def __init__(self, id, movie_name, time):
#         self.id = id
#         self.movie_name = movie_name
#         self.time = time
#         self.show_list = []
#         self.seats = {}
#         self.rows = 10
#         self.cols = 10
#         self.seat_list = []
#         for i in range(self.rows):
#             self.seat_list.append([])
#             for j in range(self.cols):
#                 self.seat_list[i].append(0)
#         self.seats[self.id] = self.seat_list

#     def show(self):
#         self.show_list.append((self.id, self.movie_name, self.time))
#         print(self.show_list)

#     def show_seats(self):
#         print(self.seats)


# hall = entry_show('1', 'Avengers', '10:00')
# hall.show()
# hall.show_seats()

# Make a method in Hall class named book_seats() which will take the customer name, phone number, an id of the show and list of tuples where every tuple contains the row and col of the seat. You need to check the id of the show, and book the seats.

class book_seats():
    def __init__(self, customer_name, phone_number, id, seat_list):
        self.customer_name = customer_name
        self.phone_number = phone_number
        self.id = id
        self.seat_list = seat_list
        self.seats = {}
        self.rows = 10
        self.cols = 10
        self.seat_list = []
        for i in range(self.rows):
            self.seat_list.append([])
            for j in range(self.cols):
                self.seat_list[i].append(0)
        self.seats[self.id] = self.seat_list

    def book(self):
        for i in self.seat_list:
            self.seats[self.id][i[0]][i[1]] = 1
        print(self.seats)

    def show_seats(self):
        print(self.seats)
    
    


hall = book_seats('Akib', '017', '1', [(1, 1), (2, 2)])
hall.book()
hall.show_seats()
