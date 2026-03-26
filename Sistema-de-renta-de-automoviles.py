cars = []

def new_car():
    name = input("Car name:")

    car = {"Car name:":name,
       "Car state": "Available" }

    cars.append(car)
    print("Car added")