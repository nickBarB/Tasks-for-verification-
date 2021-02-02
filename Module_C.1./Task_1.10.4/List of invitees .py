from Class_Volunteer import Volunteer

class List_of_invitees:
    def __init__(self, name):
        self.name = name
        guests = []
        self.guests = guests

    def get_a_name(self):
        return self.name

    def add_guest(self, guest):
        return self.guests.append(str(guest))

    def get_a_guests(self):
        if self.guests:
            print(f'\t #{self.get_a_name()}# \n{"-"*20} \nList of invitees: \n{"-"*20}')
            guests = ""
            for i in range(len(self.guests)):
                guests += f'{self.guests[i]}\n'
            return guests

guest1 = Volunteer("Ivan Petrov", "Moscow", "Mentor")
guest2 = Volunteer("Valdemar Pupkin", "Moscow", "The Imperator")
guest3 = Volunteer("Donald Trump", "Washington", "The president")

event = List_of_invitees("***Corporate party for volunteers***")
event.add_guest(guest1)
event.add_guest(guest2)
event.add_guest(guest3)
print(event.get_a_guests())