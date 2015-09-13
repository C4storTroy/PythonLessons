class Parent:
    def __init__(self, last_name, eye_color):
        print("Parent constructor")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info():
        print("Last name - " + self.last_name)
        print("Eye color - " + self.eye_color)

class Child(Parent):
    def __init__(self,last_name, eye_color, number_of_toys):
        print("Child constructor")
        Parent.__init__(self, last_name,eye_color)
        self.number_of_toys = number_of_toys
    def show_info():
        print("Last name   - " + self.last_name)
        print("Eye color   - " + self.eye_color)
        print("Number toys - " + self.number_of_toys)

mi_cyrus = Child("Cyrus", "blue", 5)
print(mi_cyrus.last_name)
print(mi_cyrus.number_of_toys)
