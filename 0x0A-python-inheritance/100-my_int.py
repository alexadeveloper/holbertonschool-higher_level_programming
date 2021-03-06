#!/usr/bin/python3


class MyInt(int):
    def __init__(self, value):
        if not isinstance(value, int):
            raise TypeError("value must be an integer")
        self.value = value

    def __eq__(self, y):
        return self.value != y

    def __ne__(self, y):
        return self.value == y
