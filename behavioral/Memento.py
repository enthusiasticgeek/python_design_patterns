#!/usr/bin/env python3
import random
import string
import time
from abc import ABC, abstractmethod


class Memento(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass

    @abstractmethod
    def get_date(self) -> float:
        pass


class ConcreteMemento(Memento):
    def __init__(self, state: str):
        self._state = state
        self._date = time.time()

    def get_state(self) -> str:
        return self._state

    def get_name(self) -> str:
        return f"{self._date} / ({self._state[:9]}...)"

    def get_date(self) -> float:
        return self._date


class Originator:
    def __init__(self, state: str):
        self._state = state
        print(f"Originator: My initial state is {self._state}")

    def do_something(self) -> None:
        print("Originator: I'm doing something important.")
        self._state = self._generate_random_string(30)
        print(f"Originator: and my state has changed to {self._state}")

    def _generate_random_string(self, length: int = 10) -> str:
        allowed_symbols = string.ascii_letters
        result = ""

        while length > 0:
            result += random.choice(allowed_symbols)
            time.sleep(0.012)
            length -= 1

        return result

    def save(self) -> Memento:
        return ConcreteMemento(self._state)

    def restore(self, memento: Memento) -> None:
        self._state = memento.get_state()
        print(f"Originator: My state has changed to {self._state}")


class Caretaker:
    def __init__(self, originator: Originator):
        self._mementos = []
        self._originator = originator

    def backup(self) -> None:
        print("\nCaretaker: Saving Originator's state...")
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        if not self._mementos:
            return

        memento = self._mementos.pop()
        print(f"Caretaker: Restoring state to {memento.get_name()}")

        try:
            self._originator.restore(memento)
        except RuntimeError:
            self.undo()

    def show_history(self) -> None:
        print("Caretaker: Here's the list of mementos:")
        for memento in self._mementos:
            print(memento.get_name())


if __name__ == "__main__":
    originator = Originator("Super-duper-super-puper-super.")
    caretaker = Caretaker(originator)

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    caretaker.backup()
    originator.do_something()

    print()
    caretaker.show_history()

    print("\nClient: Now, let's rollback!\n")
    caretaker.undo()

    print("\n\nClient: Once more!\n")
    caretaker.undo()

    del caretaker
    del originator

