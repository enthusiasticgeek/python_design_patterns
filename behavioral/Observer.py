#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message_from_subject: str) -> None:
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class ConcreteSubject(Subject):
    def __init__(self):
        self._observers = []
        self._message = ""

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self._message)

    def create_message(self, message: str = "Empty") -> None:
        self._message = message
        self.notify()

    def some_business_logic(self) -> None:
        self._message = "Changed message"
        self.notify()


class ConcreteObserver(Observer):
    _static_number = 0

    def __init__(self, subject: Subject):
        self._subject = subject
        self._subject.attach(self)
        self._number = ConcreteObserver._static_number
        ConcreteObserver._static_number += 1
        print(f"Hi, I'm the Observer \"{self._number}\".")

    def update(self, message_from_subject: str) -> None:
        self.message_from_subject_ = message_from_subject
        self.print_info()

    def attach_to_subject(self) -> None:
        self._subject.attach(self)

    def remove_me_from_the_list(self) -> None:
        self._subject.detach(self)
        print(f"Observer \"{self._number}\" removed from the list.")

    def print_info(self) -> None:
        print(f"Observer \"{self._number}\": a new message is available --> {self.message_from_subject_}")

    def __del__(self):
        self._subject.detach(self)
        print(f"Goodbye, I was the Observer \"{self._number}\".")


def client_code() -> None:
    subject = ConcreteSubject()

    subject.create_message("Welcome! :D")
    observer1 = ConcreteObserver(subject)
    observer2 = ConcreteObserver(subject)
    observer3 = ConcreteObserver(subject)

    observer1.attach_to_subject()
    observer2.attach_to_subject()
    observer3.attach_to_subject()

    observer1.remove_me_from_the_list()

    subject.create_message("Hello there!")

    observer2.remove_me_from_the_list()

    subject.some_business_logic()


if __name__ == "__main__":
    client_code()
