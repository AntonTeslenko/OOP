class BinaryNumber:
    def __init__(self, bin_numeric):
        self.bin_numeric = bin_numeric

    def __and__(self, other):
        return BinaryNumber(self.bin_numeric & other.bin_numeric)

    def __or__(self, other):
        return BinaryNumber(self.bin_numeric | other.bin_numeric)

    def __xor__(self, other):
        return BinaryNumber(self.bin_numeric ^ other.bin_numeric)

    def __invert__(self):
        return BinaryNumber(~self.bin_numeric)

    def __repr__(self):
        return bin(self.bin_numeric)


numeric1 = BinaryNumber(0b1010)
numeric2 = BinaryNumber(0b1100)

print("AND", numeric1 & numeric2)
print("OR", numeric1 | numeric2)
print("XOR", numeric1 ^ numeric2)
print("NOT numeric1", ~numeric1)
