#!/usr/bin/env python3
from abc import ABC, abstractmethod


class State(ABC):
    @abstractmethod
    def handle1(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass


class Context:
    def __init__(self):
        self._state = None

    def transition_to(self, state: State) -> None:
        print(f"Context: Transition to {type(state).__name__}.")
        self._state = state
        self._state.set_context(self)

    def request1(self) -> None:
        self._state.handle1()

    def request2(self) -> None:
        self._state.handle2()


class ConcreteStateA(State):
    def set_context(self, context: Context) -> None:
        self._context = context

    def handle1(self) -> None:
        print("ConcreteStateA handles request1.")
        print("ConcreteStateA wants to change the state of the context.")
        if self._context:
            self._context.transition_to(ConcreteStateB())
        else:
            print("Invalid reference to the context.")

    def handle2(self) -> None:
        print("ConcreteStateA handles request2.")


class ConcreteStateB(State):
    def set_context(self, context: Context) -> None:
        self._context = context

    def handle1(self) -> None:
        print("ConcreteStateB handles request1.")

    def handle2(self) -> None:
        print("ConcreteStateB handles request2.")
        print("ConcreteStateB wants to change the state of the context.")
        if self._context:
            self._context.transition_to(ConcreteStateA())
        else:
            print("Invalid reference to the context.")


def client_code() -> None:
    context = Context()
    stateA = ConcreteStateA()
    context.transition_to(stateA)

    context.request1()
    context.request2()


if __name__ == "__main__":
    client_code()
