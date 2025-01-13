"""
Objectives
improving the student's skills in operating with inheritance and composition

Scenario
Imagine that you are an automotive fan, and you are able to build a car from a limited set of components.

Your task is to :

* define classes representing:
- tires (as a bundle needed by a car to operate); methods available: get_pressure(), pump(); attribute available: size
- engine; methods available: start(), stop(), get_state(); attribute available: fuel type
- vehicle; method available: __init__(VIN, engine, tires); attribute available: VIN

* based on the classes defined above, create the following objects:
- two sets of tires: city tires (size: 15), off-road tires (size: 18)
- two engines: electric engine, petrol engine

* instantiate two objects representing cars:
- the first one is a city car, built of an electric engine and city tires
- the second one is an all-terrain car build of a petrol engine and off-road tires

* play with the cars by calling methods responsible for interaction with components.
"""


class Tires:
    def __init__(self, size):
        self.__size = size
        
    def get_pressure(self):
        pass
    
    def pump(self):
        pass
        
        
class CityTires(Tires):
    def __init__(self):
        super().__init__(15)

    def get_pressure(self):
        print(f'Pressure of city tire: 35 psi')

    def pump(self):
        print(f'Pump of city tire')
    
    
class OffRoadTires(Tires):
    def __init__(self):
        super().__init__(18)

    def get_pressure(self):
        print(f'Pressure of off road tire: 20 psi')

    def pump(self):
        print('Pump of off road tire')


class Engine:
    def __init__(self, fuel_type):
        self.__fuel_type = fuel_type
        
    def start(self):
        pass
    
    def stop(self):
        pass
    
    def get_state(self):
        pass


class ElectricEngine(Engine):
    def __init__(self):
        super().__init__('Electric Engine')
        self.state = 'init'

    def start(self):
        self.state = 'started'
        print('Starting electric engine')

    def stop(self):
        self.state = 'stopped'
        print('Stopping electric engine')

    def get_state(self):
        print(f'Getting electric engine state: {self.state}')
    
    
class PetrolEngine(Engine):
    def __init__(self):
        super().__init__('Petrol Engine')
        self.state = 'init'

    def start(self):
        self.state = 'started'
        print('Starting petrol engine')

    def stop(self):
        self.state = 'stopped'
        print('Stopping petrol engine')

    def get_state(self):
        print(f'Getting petrol engine state: {self.state}')
    
    
class Vehicle:
    def __init__(self, VIN, engine, tires):
        self.__VIN = VIN
        self.engine = engine
        self.tires = tires
        print(f'Vehicle {self.__VIN} is initialised')


city_car = Vehicle('KLAVG6929183E9LF5', ElectricEngine(), CityTires())

city_car.tires.get_pressure()
city_car.engine.get_state()
city_car.engine.start()
city_car.engine.get_state()
city_car.engine.stop()
city_car.engine.get_state()

all_terrain_car = Vehicle('WVWTG61JX2BV2RJ7D', PetrolEngine(), OffRoadTires())
all_terrain_car.tires.pump()
all_terrain_car.engine.start()
all_terrain_car.engine.get_state()
all_terrain_car.engine.stop()
all_terrain_car.engine.get_state()


# Vehicle KLAVG6929183E9LF5 is initialised
# Pressure of city tire: 35 psi
# Getting electric engine state: init
# Starting electric engine
# Getting electric engine state: started
# Stopping electric engine
# Getting electric engine state: stopped

# Vehicle WVWTG61JX2BV2RJ7D is initialised
# Pump of off road tire
# Starting petrol engine
# Getting petrol engine state: started
# Stopping petrol engine
# Getting petrol engine state: stopped
