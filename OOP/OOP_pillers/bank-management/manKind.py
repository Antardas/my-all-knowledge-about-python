""" All About Mankind """


class Human:

    def __init__(self, gender, height, weight):
        self.gender = gender
        self.height = height
        self.weight = weight


class Police(Human):

    def __init__(self, gender, height, weight, cases, nationality):
        super.__init__(gender, height, weight)
        self.cases = cases
        self.nationality = nationality
    def speak():
        pass
    
police = Police()



