class Car:
    def __init__(self, ps):
        self.ps = ps

    def __add__(self, other):
        if isinstance(other, Car):
            return self.ps + other.ps
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Car):
            return self.ps - other.ps
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Car):
            return self.ps * other.ps
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.ps == other.ps
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Car):
            return self.ps < other.ps
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Car):
            return self.ps > other.ps
        return NotImplemented

    def __str__(self):
        return f"Car with {self.ps} PS"


if __name__ == "__main__":
    a1 = Car(50)
    a2 = Car(60)

    print(f"Addition: {a1 + a2}")
    print(f"Subtraktion: {a1 - a2}")
    print(f"Multiplikation: {a1 * a2}")

    print(f"a1 == a2: {a1 == a2}")
    print(f"a1 < a2: {a1 < a2}")
    print(f"a1 > a2: {a1 > a2}")

    print(a1)
    print(a2)
