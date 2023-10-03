class Person:
  counter=1
  def __init__(self,name,country):
    self.name=name
    self.country=country
    Person.__counter=Person.__counter+1
  def greet(self):
    if self.country=="India":
      print("Namaste ", self.country)
    else:
      print("Hi hello ", self.country)
  @staticmethod
  def get_counter(self):
    return Person.__counter
p=Person("Aditya","India")
q=Person("Shyam","Japan")
#print(p.counter)
print(Person.get_counter())
