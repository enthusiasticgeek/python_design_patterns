#!/usr/bin/env python3
from abc import ABC, abstractmethod


class WritingInstrument(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcretePen(WritingInstrument):
    def operation(self) -> str:
        return "{Pen}"


class ConcretePencil(WritingInstrument):
    def operation(self) -> str:
        return "{Pencil}"


class ConcreteStylus(WritingInstrument):
    def operation(self) -> str:
        return "{Stylus}"


class WritingInstrumentCreator(ABC):
    @abstractmethod
    def factory_method(self) -> WritingInstrument:
        pass

    def scribble(self) -> str:
        product = self.factory_method()
        result = f"WritingInstrumentCreator: Scribbling with {product.operation()}"
        return result


class ConcreteWritingInstrumentCreator1(WritingInstrumentCreator):
    def factory_method(self) -> WritingInstrument:
        return ConcretePen()


class ConcreteWritingInstrumentCreator2(WritingInstrumentCreator):
    def factory_method(self) -> WritingInstrument:
        return ConcretePencil()


class ConcreteWritingInstrumentCreator3(WritingInstrumentCreator):
    def factory_method(self) -> WritingInstrument:
        return ConcreteStylus()


def writing_client_code(creator: WritingInstrumentCreator):
    print("WritingClient: I'm oblivious to the creator's class, but it still works.")
    print(creator.scribble())


if __name__ == "__main__":
    print("App: Launched with the ConcreteWritingInstrumentCreator1.")
    creator1 = ConcreteWritingInstrumentCreator1()
    writing_client_code(creator1)
    print()

    print("App: Launched with the ConcreteWritingInstrumentCreator2.")
    creator2 = ConcreteWritingInstrumentCreator2()
    writing_client_code(creator2)
    print()

    print("App: Launched with the ConcreteWritingInstrumentCreator3.")
    creator3 = ConcreteWritingInstrumentCreator3()
    writing_client_code(creator3)
