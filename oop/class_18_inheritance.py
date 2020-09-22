class InvalidOPerationError(Exception):
    pass


class Stream(object):
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


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a Network.")
