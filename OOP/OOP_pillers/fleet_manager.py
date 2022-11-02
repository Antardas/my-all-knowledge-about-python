class Bus:

    def __init__(self, route, license, driver) -> None:
        self.route = route
        self.license = license
        self.driver = driver
        self.trips = []

    def start_trip(self, start_time):
        self.trips.append(Trip(start_time))


class Driver:

    def __init__(self, name, mobile, license, address, salary) -> None:
        pass

    def drive(self):
        pass

    def take_vacation(self):
        pass

    def withdraw_salary(self):
        pass


class Passenger:

    def __init__(self, name, mobile, destination) -> None:
        self.name = name
        self.mobile = mobile
        self.destination = destination

    def purchase_ticket(self, destination, price):
        pass


class Manager:

    def __init__(self, name, mobile, department) -> None:
        pass


class Counter:

    def __init__(self, manager, location) -> None:
        pass


ovi = Passenger("Ovi", "1234567890", "Dhaka")
print(ovi.name)
