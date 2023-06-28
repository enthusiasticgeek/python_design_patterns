#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import List


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, data: List[str]) -> str:
        pass


class Context:
    def __init__(self, strategy: Strategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def do_some_business_logic(self) -> None:
        print("Context: Sorting data using the strategy (not sure how it'll do it)")
        result = self._strategy.do_algorithm(["a", "e", "c", "b", "d"])
        print(result)


class ConcreteStrategyA(Strategy):
    def do_algorithm(self, data: List[str]) -> str:
        result = "".join(data)
        result = "".join(sorted(result))
        return result


class ConcreteStrategyB(Strategy):
    def do_algorithm(self, data: List[str]) -> str:
        result = "".join(data)
        result = "".join(sorted(result))
        result = result[::-1]
        return result


def client_code() -> None:
    context = Context(ConcreteStrategyA())
    print("Client: Strategy is set to normal sorting.")
    context.do_some_business_logic()

    print()

    print("Client: Strategy is set to reverse sorting.")
    context.set_strategy(ConcreteStrategyB())
    context.do_some_business_logic()


if __name__ == "__main__":
    client_code()
