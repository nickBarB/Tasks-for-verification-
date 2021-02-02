#                                     ("\(O_o)/")
class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_a_name(self):
        return self.name

    def get_a_gender(self):
        return self.gender

    def get_a_age(self):
        return self.age

    def show_info(self):
        print("*" * 10)
        print("Name:", self.name, "\nGender:", self.gender, "\nAge:", self.age)
        print("-" * 10)
