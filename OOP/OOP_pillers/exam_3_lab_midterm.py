from argparse import OPTIONAL


class Star_Cinema():

    hall_list = []

    def __init__(self):
        pass

    def entry_hall(self, hall):
        self.hall_list.append(hall)


class Hall:

    def __init__(self, rows, cols, hall_no):
        self.__seats = {}
        # list of tuples
        self.__show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        self.__show_list.append((id, movie_name, time))
        two_d_seat_list = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(f'{chr(ord("@")+(i+1))}{j}')
            two_d_seat_list.append(row)
        self.__seats[id] = two_d_seat_list

    def book_seats(self, name, phone_number, show_id, seats):
        # seats is a list of tuples

        # check if show_id is valid
        if show_id not in self.__seats:
            print("Invalid show id")
            return

        # check if seats are valid
        for seat in seats:
            if seat[0] >= self.rows or seat[1] >= self.cols:
                print("Invalid seat")
                return

            if self.__seats[show_id][seat[0]][seat[1]] != 'free':
                print("Seat already booked")
                return

        # book seats
        for seat in seats:
            self.__seats[show_id][seat[0]][seat[1]] = (name, phone_number)

        print("Seats booked successfully")

    def view_show_list(self):
        print('-' * 100)
        for show in self.__show_list:
            print(
                f''' MOVIE NAME: {show[1]}\t\t  TIME: {show[2]} \t\t SHOW ID: {show[0]}'''
            )
        print('-' * 100)

    def view_available_seats(self, show_id):

        # check if show_id is valid
        if show_id not in self.__seats:
            print("Invalid show id")
            return

        for row in self.__seats[show_id]:
            for seat in row:
                if seat == 'free':
                    print(seat, end=' ')
                else:
                    print('booked', end=' ')
            print()
            print('_' * 100)


hall_1 = Hall(5, 5, 1)

hall_1.entry_show(1, "Avengers", "10/11/22 10:00 AM")
hall_1.entry_show(2, "Avengers", "11/11/22 12:00 PM")
hall_1.entry_show(3, "Avengers", "12/11/22 2:00 PM")

hall_1.book_seats("Antar", 12345, 1, [(0, 0), (0, 1), (0, 2)])

# print(hall_1.seats)

while (True):
    print("1. VIEW ALL SHOWS TODAY")
    print("2. VIEW AVAILABLE SEATS")
    print("3. BOOK SEATS")
    option = int(input("ENTER OPTIONS: "))
    if option == 1:
        hall_1.view_show_list()
    elif option == 2:
        show_id = int(input("ENTER SHOW ID: "))
        hall_1.view_available_seats(show_id)
    elif option == 3:
        name = input("ENTER NAME: ")
        phone_number = int(input("ENTER PHONE NUMBER: "))
        show_id = int(input("ENTER SHOW ID: "))
        seats = []
        while (True):
            row = int(input("ENTER ROW: "))
            col = int(input("ENTER COL: "))
            seats.append((row, col))
            if input("DO YOU WANT TO ADD MORE SEATS? (y/n): ") == 'n':
                break
        hall_1.book_seats(name, phone_number, show_id, seats)
    else:
        break
