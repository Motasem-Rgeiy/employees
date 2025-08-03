from abc import abstractmethod
class Car:
    def __init__(self , model , color):
        self.model = model
        self.color = color
    
    def info(self):
        print(f'Model:{self.model},Color:{self.color}')
    
class Toyota(Car):
    def move(self):
        print('Slow')

class Pogati(Car):
    def move(self):
        print('Fast')

class Accent(Car):
    def move(self):
        print('Slow')

toyota = Toyota('2005' , 'Red')
pogati = Pogati('2012' , "Black")
accent = Accent('2021' , 'Blue')

for car in [toyota , pogati , accent]:
    car.info()    


