#!/usr/bin/env python3
class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready!\n"

    def operationN(self) -> str:
        return "Subsystem1: Go!\n"

class Subsystem2:
    def operation1(self) -> str:
        return "Subsystem2: Get ready!\n"

    def operationZ(self) -> str:
        return "Subsystem2: Fire!\n"

class Facade:
    def __init__(self, subsystem1=None, subsystem2=None):
        self.subsystem1 = subsystem1 or Subsystem1()
        self.subsystem2 = subsystem2 or Subsystem2()

    def operation(self) -> str:
        result = "Facade initializes subsystems:\n"
        result += self.subsystem1.operation1()
        result += self.subsystem2.operation1()
        result += "Facade orders subsystems to perform the action:\n"
        result += self.subsystem1.operationN()
        result += self.subsystem2.operationZ()
        return result

def client_code(facade):
    print(facade.operation())

if __name__ == "__main__":
    subsystem1 = Subsystem1()
    subsystem2 = Subsystem2()
    facade = Facade(subsystem1, subsystem2)
    client_code(facade)
