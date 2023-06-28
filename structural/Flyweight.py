#!/usr/bin/env python3
import copy
from typing import List

class SharedState:
    def __init__(self, brand: str, model: str, color: str):
        self.brand = brand
        self.model = model
        self.color = color

    def __str__(self) -> str:
        return f"[ {self.brand} , {self.model} , {self.color} ]"

class UniqueState:
    def __init__(self, owner: str, plates: str):
        self.owner = owner
        self.plates = plates

    def __str__(self) -> str:
        return f"[ {self.owner} , {self.plates} ]"

class Flyweight:
    def __init__(self, shared_state: SharedState):
        self.shared_state = shared_state

    def operation(self, unique_state: UniqueState) -> None:
        print(f"Flyweight: Displaying shared ({self.shared_state}) and unique ({unique_state}) state.")

class FlyweightFactory:
    def __init__(self, shared_states: List[SharedState]):
        self.flyweights = {}
        for shared_state in shared_states:
            key = self.get_key(shared_state)
            self.flyweights[key] = Flyweight(copy.deepcopy(shared_state))

    def get_key(self, shared_state: SharedState) -> str:
        return f"{shared_state.brand}_{shared_state.model}_{shared_state.color}"

    def get_flyweight(self, shared_state: SharedState) -> Flyweight:
        key = self.get_key(shared_state)
        if key not in self.flyweights:
            print("FlyweightFactory: Can't find a flyweight, creating a new one.")
            self.flyweights[key] = Flyweight(copy.deepcopy(shared_state))
        else:
            print("FlyweightFactory: Reusing existing flyweight.")
        return self.flyweights[key]

    def list_flyweights(self) -> None:
        count = len(self.flyweights)
        print(f"\nFlyweightFactory: I have {count} flyweights:")
        for key in self.flyweights:
            print(key)

def add_car_to_police_database(
    factory: FlyweightFactory, plates: str, owner: str, brand: str, model: str, color: str
) -> None:
    print("\nClient: Adding a car to the database.")
    shared_state = SharedState(brand, model, color)
    flyweight = factory.get_flyweight(shared_state)
    flyweight.operation(UniqueState(owner, plates))

if __name__ == "__main__":
    factory = FlyweightFactory([
        SharedState("Chevrolet", "Camaro2018", "pink"),
        SharedState("Mercedes Benz", "C300", "black"),
        SharedState("Mercedes Benz", "C500", "red"),
        SharedState("BMW", "M5", "red"),
        SharedState("BMW", "X6", "white"),
    ])

    factory.list_flyweights()

    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "M5", "red")
    add_car_to_police_database(factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    factory.list_flyweights()
