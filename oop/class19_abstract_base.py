# Abstract Base Class
'''
There are some issues with this implementation:
1. We are only using Stream class so that we can use
   common methods among it's different child classes.
   We shouldn't be able to acces it but we can create
   it's instance.
2. Both the derived classes have a read function and
for now there is no way to wrap them up in one place.

What we'll do is make the 'Stream' class an abstract class.
When a class has an abstract method. it becomes an abstract
class and we cannot instantiate it.
    If a class derives from an abstract class, it has to have
that abstract method otherwise it'll be considered an abstract
class too. And therefore we won't be able to instactiate it as well.
'''
from abc import ABC, abstractmethod
class InvalidOPerationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOPerationError("Stream is already Opened.")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOPerationError("Stream is already Closed.")
        self.opened = False

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network.")


class MemoryStream(Stream):
    def read(self):
        print("Reading from a memory stream.")
# stream = Stream() Stream is an abstract class so we cannot instantiate it. This will give an error.

