#!/usr/bin/env python3
from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class SimpleCommand(Command):
    def __init__(self, payload):
        self.payload = payload

    def execute(self):
        print(f"SimpleCommand: See, I can do simple things like printing ({self.payload})")


class Receiver:
    def do_something(self, a):
        print(f"Receiver: Working on ({a}.)")

    def do_something_else(self, b):
        print(f"Receiver: Also working on ({b}.)")


class ComplexCommand(Command):
    def __init__(self, receiver, a, b):
        self.receiver = receiver
        self.a = a
        self.b = b

    def execute(self):
        print("ComplexCommand: Complex stuff should be done by a receiver object.")
        self.receiver.do_something(self.a)
        self.receiver.do_something_else(self.b)


class Invoker:
    def __init__(self):
        self.on_start = None
        self.on_finish = None

    def set_on_start(self, command):
        self.on_start = command

    def set_on_finish(self, command):
        self.on_finish = command

    def do_something_important(self):
        print("Invoker: Does anybody want something done before I begin?")
        if self.on_start:
            self.on_start.execute()
        print("Invoker: ...doing something really important...")
        print("Invoker: Does anybody want something done after I finish?")
        if self.on_finish:
            self.on_finish.execute()


if __name__ == '__main__':
    invoker = Invoker()
    invoker.set_on_start(SimpleCommand("Say Hi!"))
    receiver = Receiver()
    invoker.set_on_finish(ComplexCommand(receiver, "Send email", "Save report"))
    invoker.do_something_important()
