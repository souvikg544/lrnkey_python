
class rectangle:

    def area(self,length,breadth):
        area=length*breadth
        print("Area :",area)

    def perimeter(self,length,breadth):
        per=2*(length+breadth)
        print("Perimeter = ", per)

rec=rectangle()
rec.area(8,5)
rec.perimeter(8,5)


