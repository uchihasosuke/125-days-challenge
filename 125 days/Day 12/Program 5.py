#Implement a Python ADT for a set, including methods for union, intersection, and difference.
class MySet:
    def __init__(self):
        self.elements = []

    def add(self, element):
        if element not in self.elements:
            self.elements.append(element)

    def remove(self, element):
        if element in self.elements:
            self.elements.remove(element)

    def union(self, other_set):
        new_set = MySet()
        new_set.elements = self.elements.copy()

        for element in other_set.elements:
            if element not in new_set.elements:
                new_set.elements.append(element)

        return new_set

    def intersection(self, other_set):
        new_set = MySet()

        for element in self.elements:
            if element in other_set.elements:
                new_set.add(element)

        return new_set

    def difference(self, other_set):
        new_set = MySet()

        for element in self.elements:
            if element not in other_set.elements:
                new_set.add(element)

        return new_set

    def display(self):
        print("Set elements:", self.elements)
