from models.person import Person
from models.table import Table
from models.openspace import OpenSpace

def main():
    os = OpenSpace("BeCode Workspace")

    t1 = Table("Table A", 3)
    t2 = Table("Table B", 2)
    os.add_table(t1)
    os.add_table(t2)

    p1 = Person("Alice", "developer")
    p2 = Person("Bob", "coach")
    p3 = Person("Charlie", "developer")

    os.assign_person(p1)
    os.assign_person(p2)
    os.assign_person(p3)

    os.display()

if __name__ == "__main__":
    main()
