
class Calculator:

    def plus(self, a, b):
        return float(a + b)

    def minus(self, a, b):
        return float(a - b)

    def multi(self, a, b):
        return float(a * b)

    def div(self, a, b):
        if a or b != 0:
            return float(a / b)
        else:
            print("Error деление на 0")

