#!/usr/bin/env python3
from abc import ABC, abstractmethod
from datetime import datetime

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request.")

class Proxy(Subject):
    def __init__(self, real_subject):
        self.real_subject = real_subject

    def check_access(self):
        # Some real checks should go here.
        print("Proxy: Checking access prior to firing a real request.")
        return True

    def log_access(self):
        print("Proxy: Logging the time of request.")

    def request(self):
        if self.check_access():
            self.real_subject.request()
            self.log_access()

def client_code(subject):
    subject.request()

if __name__ == "__main__":
    print("Client: Executing the client code with a real subject:")
    real_subject = RealSubject()
    client_code(real_subject)

    print("\n")

    print("Client: Executing the same client code with a proxy:")
    proxy = Proxy(real_subject)
    client_code(proxy)
