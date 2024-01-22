class Calculator:
    def __init__(self):
        self.history = []

    def add(self, num1, num2):
        result = num1 + num2
        self.history.append(f"added {num1} to {num2} got {result}")
        return result

    def multiply(self, num1, num2):
        result = num1 * num2
        self.history.append(f"multiplied {num1} to {num2} got {result}")
        return result

    def print_operations(self):
        for operation in self.history:
            print(operation)


c = Calculator()
out = c.add(3, 5)
print(out)

out = c.add(10, 20)
print(out)

c.print_operations()
