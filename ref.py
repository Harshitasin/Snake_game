#object without reference
class Person:
    def __init__(self, name_ip, country_ip):
        self.name = name_ip
        self.country = country_ip
p=Person()#p is obj till now---->not
#by calling person one object has been created and inside p we'll only store memory adress of that object
#p is not obj it contains reference/adress of obj
