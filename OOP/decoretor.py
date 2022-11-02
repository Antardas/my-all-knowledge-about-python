def timer(func):
    def inner():
        print("Start")
        func()
        print("End")
    return inner

@timer
def get_facebook():
    print("Getting Facebook")


get_facebook()