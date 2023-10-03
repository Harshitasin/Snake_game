#How objects access attributes
class Person:
    def __init__(self, name_ip, country_ip):
        self.name = name_ip
        self.country = country_ip
    def greet(self):
        if self.country =="India":
            print("namaste ",self.name)
        else:
            print("hello",self.name)
#how
p1=Person("X","China")
print(p1.greet())
#what if i try to access non-existence attributes
#p.gender------>error
p1.gender="male"
print(p1.gender)