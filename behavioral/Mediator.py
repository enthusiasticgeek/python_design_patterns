#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Mediator:
    @abstractmethod
    def notify(self, sender: 'BaseComponent', event: str) -> None:
        pass


class BaseComponent(ABC):
    def __init__(self, mediator: Mediator = None):
        self._mediator = mediator

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class Component1(BaseComponent):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self._mediator.notify(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self._mediator.notify(self, "B")


class Component2(BaseComponent):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self._mediator.notify(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self._mediator.notify(self, "D")


class ConcreteMediator(Mediator):
    def __init__(self, component1: Component1, component2: Component2):
        self._component1 = component1
        self._component2 = component2

    def notify(self, sender: BaseComponent, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers the following operations:")
            self._component2.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers the following operations:")
            self._component1.do_b()
            self._component2.do_c()


def client_code() -> None:
    component1 = Component1()
    component2 = Component2()
    mediator = ConcreteMediator(component1, component2)

    component1.mediator = mediator
    component2.mediator = mediator

    print("Client triggers operation A.")
    component1.do_a()
    print()
    print("Client triggers operation D.")
    component2.do_d()


if __name__ == "__main__":
    client_code()
