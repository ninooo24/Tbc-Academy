class Inset:
    def __init__(self):
        self.elements = []

    def insert(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def member(self, element):
        return element in self.elements

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)
        else:
            raise ValueError("ვერ ვიპოვნე")

    def __str__(self):
        return ', '.join(map(str, sorted(self.elements)))


inset = Inset()
inset.insert(8)
inset.insert(15)
inset.insert(3)
inset.insert(2)

print(inset)

print(inset.member(3))
print(inset.member(35))

inset.remove(3)
print(inset)


