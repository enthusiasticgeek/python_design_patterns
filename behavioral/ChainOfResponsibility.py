#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Handler(ABC):
    @abstractmethod
    def set_next(self, handler):
        pass

    @abstractmethod
    def handle(self, request):
        pass

class AbstractHandler(Handler):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)
        return ''

class MonkeyHandler(AbstractHandler):
    def handle(self, request):
        if request == "Banana":
            return f"Monkey: I'll eat the {request}.\n"
        else:
            return super().handle(request)

class SquirrelHandler(AbstractHandler):
    def handle(self, request):
        if request == "Nut":
            return f"Squirrel: I'll eat the {request}.\n"
        else:
            return super().handle(request)

class DogHandler(AbstractHandler):
    def handle(self, request):
        if request == "MeatBall":
            return f"Dog: I'll eat the {request}.\n"
        else:
            return super().handle(request)

def client_code(handler):
    food = ["Nut", "Banana", "Cup of coffee"]
    for f in food:
        print(f"Client: Who wants a {f}?")
        result = handler.handle(f)
        if result:
            print(f"  {result}")
        else:
            print(f"  {f} was left untouched.")

if __name__ == '__main__':
    monkey = MonkeyHandler()
    squirrel = SquirrelHandler()
    dog = DogHandler()
    monkey.set_next(squirrel).set_next(dog)

    print("Chain: Monkey > Squirrel > Dog\n")
    client_code(monkey)
    print()
    print("Subchain: Squirrel > Dog\n")
    client_code(squirrel)
