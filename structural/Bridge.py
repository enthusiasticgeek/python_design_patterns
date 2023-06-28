#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Implementation(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass

class ConcreteImplementationA(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationA: Here's the result on the platform A.\n"

class ConcreteImplementationB(Implementation):
    def operation_implementation(self):
        return "ConcreteImplementationB: Here's the result on the platform B.\n"

class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def operation(self):
        return f"Abstraction: Base operation with:\n{self.implementation.operation_implementation()}"

class ExtendedAbstraction(Abstraction):
    def operation(self):
        return f"ExtendedAbstraction: Extended operation with:\n{self.implementation.operation_implementation()}"

def client_code(abstraction):
    print(abstraction.operation())

if __name__ == "__main__":
    implementation_a = ConcreteImplementationA()
    abstraction_a = Abstraction(implementation_a)
    client_code(abstraction_a)
    implementation_b = ConcreteImplementationB()
    abstraction_b = Abstraction(implementation_b)
    client_code(abstraction_b)
