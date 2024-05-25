class ExtendedList(list):
    def min(self):
        if not self:
            raise ValueError("List is empty")
        return min(self)

    def max(self):
        if not self:
            raise ValueError("List is empty")
        return max(self)


el_1 = ExtendedList([14, 1, 4, 5, 8, 9])
el_2 = ExtendedList([-7, 5, -3, 2, 0, -1])

print("element 1: ", el_1)
print("min:", el_1.min())
print("max:", el_1.max())

print("element 2: ", el_2)
print("min:", el_2.min())
print("max:", el_2.max())

