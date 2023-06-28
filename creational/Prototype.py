#!/usr/bin/env python3
from abc import ABC, abstractmethod
from enum import Enum
import copy


class Type(Enum):
    PROTOTYPE_1 = 0
    PROTOTYPE_2 = 1


class Prototype(ABC):
    def __init__(self, prototype_name):
        self.prototype_name = prototype_name
        self.prototype_field = None

    @abstractmethod
    def clone(self):
        pass

    def method(self, prototype_field):
        self.prototype_field = prototype_field
        print(f"Call Method from {self.prototype_name} with field: {self.prototype_field}")


class ConcretePrototype1(Prototype):
    def __init__(self, prototype_name, concrete_prototype_field):
        super().__init__(prototype_name)
        self.concrete_prototype_field1 = concrete_prototype_field

    def clone(self):
        return copy.deepcopy(self)


class ConcretePrototype2(Prototype):
    def __init__(self, prototype_name, concrete_prototype_field):
        super().__init__(prototype_name)
        self.concrete_prototype_field2 = concrete_prototype_field

    def clone(self):
        return copy.deepcopy(self)


class PrototypeFactory:
    def __init__(self):
        self.prototypes = {
            Type.PROTOTYPE_1: ConcretePrototype1("PROTOTYPE_1", 50.0),
            Type.PROTOTYPE_2: ConcretePrototype2("PROTOTYPE_2", 60.0)
        }

    def create_prototype(self, type):
        return self.prototypes[type].clone()


def client(prototype_factory):
    print("Let's create a Prototype 1")
    prototype = prototype_factory.create_prototype(Type.PROTOTYPE_1)
    prototype.method(90)
    print()

    print("Let's create a Prototype 2")
    prototype = prototype_factory.create_prototype(Type.PROTOTYPE_2)
    prototype.method(10)


if __name__ == "__main__":
    prototype_factory = PrototypeFactory()
    client(prototype_factory)
