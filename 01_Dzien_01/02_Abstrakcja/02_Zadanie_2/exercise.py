import math


# __len__, __getitem__
def middle_elements(sequences):
    result = []

    for sequence in sequences:
        if len(sequence) != 0:
            middle_idx = len(sequence) // 2
            middle_element = sequence[middle_idx]
            result.append(middle_element)

    return result


# Protokół
# len()  # -> __len__
# []  # -> __getitem__


class SequanceOfNumbers:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step

    def __len__(self):
        return math.ceil((self.stop - self.start) / self.step)

    def __getitem__(self, idx):
        if idx < 0 or idx >= math.ceil((self.stop - self.start) / self.step):
            raise IndexError("Index out of range")

        return self.start + idx * self.step


s = SequanceOfNumbers(1, 6, 1)

res = middle_elements([
    [6, 7, 8, 9, 10],  # środkowy element to 8
    ["Kto", "to", "taki?"],  # środkowy element to "to"
    [],  # pusto - pomijamy
    # środkowe elementy to "siedem" oraz "osiem" - wybieramy "osiem"
    ["sześć", "siedem", "osiem", "dziewięć"],
    (1,2,3),
    "asdqwe",
    s
])
print(res)
