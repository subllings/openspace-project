class OpenSpace:
    def __init__(self, name):
        self.name = name
        self.tables = []

    def add_table(self, table):
        self.tables.append(table)

    def assign_person(self, person):
        for table in self.tables:
            if not table.is_full():
                return table.add_person(person)
        return False

    def display(self):
        print(f"Open Space: {self.name}")
        for table in self.tables:
            print(table)
