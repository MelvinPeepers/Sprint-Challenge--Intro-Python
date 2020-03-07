# Write classes for the following class hierarchy:

#     [Vehicle] -> [FlightVehicle] -> [Starship]
#     | |
#     v                v
# [GroundVehicle][Airplane]
# | |
# v       v
# [Car][Motorcycle]

# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.

# e.g.


# class Whatever:
#     pass


# Put a comment noting which class is the base class


class Vehicle:  # parent / base / super class
    pass


class FlightVehicle(Vehicle):  # child class
    pass


class Starship(FlightVehicle):  # grandchild class
    pass


class Airplane(FlightVehicle):  # grandchild class
    pass


class GroundVehicle(Vehicle):  # child class
    pass


class Car(GroundVehicle):  # grandchild class
    pass


class Motorcycle(GroundVehicle):  # grandchild class
    pass
