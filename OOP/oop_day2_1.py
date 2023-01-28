
## Constructor


class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def display(self):
        print("Length : ", self.length)
        print("Breadth : ", self.breadth)
    def area(self):
        area= self.length * self.breadth
        print("Area : " , area)
    def perimeter(self):
        per=2* (self.length+self.breadth)
        print("Perimeter = ", per)

rec=rectangle(12,7)
rec.display()

rec.area()
rec.perimeter()
