from abc import ABC

from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if not self.started and self.fuel == 0:
            raise LowFuelError
        self.started = True

    def move(self, distance):
        fuel_need = distance * self.fuel_consumption
        if fuel_need > self.fuel:
            raise NotEnoughFuel
        self.fuel -= fuel_need
