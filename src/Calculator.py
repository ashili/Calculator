def addition(a, b):
    c = a + b
    return c


def substraction(a, b):
    c = a - b
    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def substract(self, a, b):
        self.result = substraction(a, b)
        return self.result
