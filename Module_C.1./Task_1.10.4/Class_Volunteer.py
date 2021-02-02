from Class_Individ import Individual

class Volunteer(Individual):
    def __init__(self, name, city, status):
        Individual.__init__(self, name, city)
        self.status = status

    def get_a_status(self):
        return self.status

    def __str__(self):
        return f'{self.get_a_name()}. \nCity: {self.get_a_city()}. \nStatus: "{self.get_a_status()}"'

