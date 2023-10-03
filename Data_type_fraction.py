class Fraction:
    #parameterized constructor
    def __init__(self,x,y):
        self.num=x
        self.Den=y
    def __str__(self):
        return "{}/{}".format(self.num,self.Den)
    def __add__(self,other):
        new_num=(self.num*other.Den)+(other.num*self.Den)
        new_Den=self.Den*other.Den
        form=new_num%new_Den
        if form==0:
            return new_num/new_Den
        return "{}/{}".format(new_num, new_Den)
    def __sub__(self, other):
        new_num = (self.num * other.Den) - (other.num * self.Den)
        new_Den = self.Den * other.Den
        if new_num==0:
            return 0
        form = new_num % new_Den
        if form == 0:
            return new_num / new_Den
        return "{}/{}".format(new_num, new_Den)
fr1=Fraction(9,1)
fr2=Fraction(1,2)
print(fr1+fr2)