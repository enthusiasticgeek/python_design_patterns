#!/usr/bin/env python3
from abc import ABC, abstractmethod


class AbstractCompact(ABC):
    @abstractmethod
    def useful_function_a(self) -> str:
        pass


class ConcreteCorolla(AbstractCompact):
    def useful_function_a(self) -> str:
        return "The result of the product: Toyota Corolla."


class ConcreteCivic(AbstractCompact):
    def useful_function_a(self) -> str:
        return "The result of the product: Honda Civic."


class AbstractMidSize(ABC):
    @abstractmethod
    def useful_function_b(self) -> str:
        pass

    @abstractmethod
    def another_useful_function_b(self, collaborator: AbstractCompact) -> str:
        pass


class ConcreteCamry(AbstractMidSize):
    def useful_function_b(self) -> str:
        return "The result of the product: Toyota Camry."

    def another_useful_function_b(self, collaborator: AbstractCompact) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B1 collaborating with ({result})"


class ConcreteAccord(AbstractMidSize):
    def useful_function_b(self) -> str:
        return "The result of the product: Honda Accord."

    def another_useful_function_b(self, collaborator: AbstractCompact) -> str:
        result = collaborator.useful_function_a()
        return f"The result of the B2 collaborating with ({result})"


class AbstractFactory(ABC):
    @abstractmethod
    def create_compact(self) -> AbstractCompact:
        pass

    @abstractmethod
    def create_mid_size(self) -> AbstractMidSize:
        pass


class ConcreteToyota(AbstractFactory):
    def create_compact(self) -> AbstractCompact:
        return ConcreteCorolla()

    def create_mid_size(self) -> AbstractMidSize:
        return ConcreteCamry()


class ConcreteHonda(AbstractFactory):
    def create_compact(self) -> AbstractCompact:
        return ConcreteCivic()

    def create_mid_size(self) -> AbstractMidSize:
        return ConcreteAccord()


def client_code(factory: AbstractFactory) -> None:
    compact = factory.create_compact()
    mid_size = factory.create_mid_size()
    print(mid_size.useful_function_b())
    print(mid_size.another_useful_function_b(compact))


if __name__ == "__main__":
    print("Client: Testing client code with the first factory type:")
    toyota = ConcreteToyota()
    client_code(toyota)
    print()

    print("Client: Testing the same client code with the second factory type:")
    honda = ConcreteHonda()
    client_code(honda)
