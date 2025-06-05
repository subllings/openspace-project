class Table:
    def __init__(self, id, capacity):
        self.id = id
        self.capacity = capacity
        self.occupants = []

    def add_person(self, person):
        if not self.is_full():
            self.occupants.append(person)
            return True
        return False

    def remove_person(self, person):
        self.occupants.remove(person)

    def is_full(self):
        return len(self.occupants) >= self.capacity

    def __str__(self):
        occupants_str = ", ".join(str(p) for p in self.occupants)
        return f"[{self.id}] {occupants_str} - {self.capacity - len(self.occupants)} free seats"
