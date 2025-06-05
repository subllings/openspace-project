from models.person import Person
from models.table import Table
from models.openspace import OpenSpace

def afficher_menu():
    print("\n====== OPEN SPACE MANAGER ======")
    print("1. Add table")
    print("2. Add person")
    print("3. Assign person to a table")
    print("4. Show open space status")
    print("5. Exit")
    print("================================")

def main():
    openspace = OpenSpace("BeCode Open Space")
    persons = []

    while True:
        afficher_menu()
        choix = input("Choose an option: ")

        if choix == "1":
            table_id = input("Enter table name: ")
            capacity = int(input("Enter table capacity: "))
            table = Table(table_id, capacity)
            openspace.add_table(table)
            print(f"Table '{table_id}' with {capacity} seats added.")

        elif choix == "2":
            name = input("Enter person's name: ")
            role = input("Enter role (e.g., developer, coach): ")
            person = Person(name, role)
            persons.append(person)
            print(f"Person '{name}' added.")

        elif choix == "3":
            if not persons:
                print("No persons available to assign.")
                continue

            for idx, person in enumerate(persons):
                print(f"{idx + 1}. {person}")
            index = int(input("Select person number to assign: ")) - 1

            if 0 <= index < len(persons):
                person = persons.pop(index)
                success = openspace.assign_person(person)
                if success:
                    print(f"{person.name} assigned to a table.")
                else:
                    print(f"No free table found for {person.name}.")
            else:
                print("Invalid selection.")

        elif choix == "4":
            openspace.display()

        elif choix == "5":
            print("Exiting Open Space Manager. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1–5.")

if __name__ == "__main__":
    main()
