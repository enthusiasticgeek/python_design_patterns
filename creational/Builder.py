#!/usr/bin/env python3
from typing import List

class RAV4:
    def __init__(self):
        self.parts: List[str] = []

    def list_parts(self):
        print("Product parts: " + ", ".join(self.parts) + "\n")


class Builder:
    def base_model(self):
        pass

    def blind_spot_monitoring(self):
        pass

    def lane_deviation_alert(self):
        pass


class ConcreteBuilder1(Builder):
    def __init__(self):
        self.product = RAV4()
        self.reset()

    def reset(self):
        self.product = RAV4()

    def base_model(self):
        self.product.parts.append("RAV4 BASE MODEL")

    def blind_spot_monitoring(self):
        self.product.parts.append("Blind Spot Monitoring")

    def lane_deviation_alert(self):
        self.product.parts.append("Lane Deviation Alert")

    def get_product(self) -> RAV4:
        result = self.product
        self.reset()
        return result


class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder: Builder):
        self.builder = builder

    def build_minimal_viable_product(self):
        self.builder.base_model()

    def build_full_featured_product(self):
        self.builder.base_model()
        self.builder.blind_spot_monitoring()
        self.builder.lane_deviation_alert()


def client_code(director: Director):
    builder = ConcreteBuilder1()
    director.set_builder(builder)

    print("Standard basic product:")
    director.build_minimal_viable_product()
    product = builder.get_product()
    product.list_parts()

    print("Standard full featured product:")
    director.build_full_featured_product()
    product = builder.get_product()
    product.list_parts()

    print("Custom product:")
    builder.base_model()
    builder.lane_deviation_alert()
    product = builder.get_product()
    product.list_parts()


if __name__ == "__main__":
    director = Director()
    client_code(director)
