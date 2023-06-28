#!/usr/bin/env python3
from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def add(self, component):
        pass

    def remove(self, component):
        pass

    def is_composite(self):
        return False

    @abstractmethod
    def operation(self):
        pass

class Leaf(Component):
    def operation(self):
        return "Leaf"

class Composite(Component):
    def __init__(self):
        super().__init__()
        self.children = []

    def add(self, component):
        self.children.append(component)
        component.set_parent(self)

    def remove(self, component):
        self.children.remove(component)
        component.set_parent(None)

    def is_composite(self):
        return True

    def operation(self):
        result = []
        for index, child in enumerate(self.children):
            result.append(child.operation())
            if index < len(self.children) - 1:
                result.append("+")
        return "Branch(" + "".join(result) + ")"

def client_code(component):
    print("RESULT: " + component.operation())

def client_code2(component1, component2):
    if component1.is_composite():
        component1.add(component2)
    print("RESULT: " + component1.operation())

if __name__ == "__main__":
    simple = Leaf()
    print("Client: I've got a simple component:")
    client_code(simple)
    print()

    tree = Composite()
    branch1 = Composite()

    leaf1 = Leaf()
    leaf2 = Leaf()
    leaf3 = Leaf()
    branch1.add(leaf1)
    branch1.add(leaf2)
    branch2 = Composite()
    branch2.add(leaf3)
    tree.add(branch1)
    tree.add(branch2)
    print("Client: Now I've got a composite tree:")
    client_code(tree)
    print()

    print("Client: I don't need to check the components classes even when managing the tree:")
    client_code2(tree, simple)
