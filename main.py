class Person:
    name = ''
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        print("Walking")

    def call(self):
        print("Calling")


class Employed(Person):
    occupation = 'Unemployment'
    salary = 0

    def __init__(self, name, age, occupation, salary):
        Person.__init__(self, name, age)
        self.occupation = occupation
        self.salary = salary

    def work_call(self):
        print("The employed is working")
        self.walk()

        self.call()
        print("The employed is calling")


employed_1 = Employed("Alejandro", 25, "Developer", 2000)

employed_1.work_call()
