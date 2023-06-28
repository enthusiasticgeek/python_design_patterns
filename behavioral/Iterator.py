#!/usr/bin/env python3
from typing import TypeVar, List, Iterator

T = TypeVar('T')


class Iterator:
    def __init__(self, collection: 'Container', reverse: bool = False):
        self.collection = collection
        self.reverse = reverse
        self.index = len(collection.data) - 1 if reverse else 0

    def __next__(self) -> T:
        try:
            result = self.collection.data[self.index]
            self.index += -1 if self.reverse else 1
            return result
        except IndexError:
            raise StopIteration()

    def __iter__(self) -> 'Iterator':
        return self


class Container:
    def __init__(self):
        self.data: List[T] = []

    def add(self, item: T) -> None:
        self.data.append(item)

    def create_iterator(self, reverse: bool = False) -> Iterator:
        return Iterator(self, reverse)


class Data:
    def __init__(self, a: int = 0):
        self.data = a

    def set_data(self, a: int) -> None:
        self.data = a

    def get_data(self) -> int:
        return self.data


def client_code():
    print("________________Iterator with int______________________________________")
    cont = Container()

    for i in range(10):
        cont.add(i)

    it = cont.create_iterator()
    for item in it:
        print(item)

    cont2 = Container()
    a = Data(100)
    b = Data(1000)
    c = Data(10000)
    cont2.add(a)
    cont2.add(b)
    cont2.add(c)

    print("________________Iterator with custom Class______________________________")
    it2 = cont2.create_iterator()
    for item in it2:
        print(item.get_data())


if __name__ == '__main__':
    client_code()
