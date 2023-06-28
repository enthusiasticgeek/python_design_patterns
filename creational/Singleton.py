#!/usr/bin/env python3
import threading
import time

class Singleton:
    _singleton_lock = threading.Lock()
    _singleton_instance = None

    def __init__(self, value):
        self.value = value

    @classmethod
    def get_instance(cls, value):
        if not cls._singleton_instance:
            with cls._singleton_lock:
                if not cls._singleton_instance:
                    cls._singleton_instance = cls(value)
        return cls._singleton_instance

    def some_business_logic(self):
        pass
        # ...


def thread_foo():
    time.sleep(1)
    singleton = Singleton.get_instance("FOO")
    print(singleton.value)


def thread_bar():
    time.sleep(1)
    singleton = Singleton.get_instance("BAR")
    print(singleton.value)


if __name__ == "__main__":
    print("If you see the same value, then singleton was reused (yay!)\n"
          "If you see different values, then 2 singletons were created (booo!!)\n\n"
          "RESULT:")
    t1 = threading.Thread(target=thread_foo)
    t2 = threading.Thread(target=thread_bar)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

