# Object Oriented Programming Day 1

class car:
    def car_types(self):
        car_list=["bmw","audi","mercedes","porche"]
        print(car_list)

    def car_cost(self):
        car_cost=[45,67,85,94]
        for i in car_cost:
            print(f"${i}K")
    def car_mileage(self,s):
        if(s==1):
            print("Mileage is 60")
        else:
            print("Mileage is 40")



car_object=car()
car_object.car_types()
car_object.car_cost()
car_object.car_mileage(1)



