# funckja generatorwa
def _range(n):
    counter = 0
    while counter < n:
        yield counter
        counter += 1


# funkcja generatorowa zwraca generator
# x = _range(100)

for item in _range(100000):
    print(item)

# A pod spodem pętla for woła funkcję next (a dokładnie metodę __next__)
# print(next(x))
# print(next(x))
# print(next(x))
