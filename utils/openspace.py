import random
from typing import List
from utils.table import Table


class Openspace:
    def __init__(self, number_of_tables: int, table_capacity: int) -> None:
        # Create tables based on the given configuration
        self.number_of_tables: int = number_of_tables
        self.tables: List[Table] = [Table(table_capacity) for _ in range(number_of_tables)]

    def organize(self, names: List[str]) -> None:
        """
        Randomly assign each person to a seat in the available tables.

        :param names: List of names to assign
        """
        import random
        random.shuffle(names)  # Shuffle names for fairness
        unassigned = []

        for name in names:
            tables_shuffled = self.tables[:]        # Make a copy of tables
            random.shuffle(tables_shuffled)         # Shuffle the table order

            assigned = False
            for table in tables_shuffled:
                if table.assign_seat(name):
                    assigned = True
                    break

            if not assigned:
                unassigned.append(name)

        if unassigned:
            print("\n>>> Could not assign the following people (no available seats):")
            for name in unassigned:
                print(f" - {name}")
            print("")


    def display(self) -> None:
        """
        Print the seating arrangement.
        """
        for index, table in enumerate(self.tables, start=1):
            print(f"Table {index}:")
            for seat_index, seat in enumerate(table.seats, start=1):
                status = seat.occupant if not seat.free else "Free"
                print(f"  Seat {seat_index}: {status}")
            
            occupants = [seat.occupant for seat in table.seats if not seat.free]
            if len(occupants) == 1:
                print(f"> Note: {occupants[0]} is sitting alone at this table.")

            print("")

    def store(self, filename: str) -> None:
        """
        Save the current seating plan to a CSV file.

        :param filename: Output file path
        """
        import csv
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Table', 'Seat', 'Occupant'])

            for table_index, table in enumerate(self.tables, start=1):
                for seat_index, seat in enumerate(table.seats, start=1):
                    writer.writerow([table_index, seat_index, seat.occupant if not seat.free else "Free"])

    def seats_left(self) -> int:
        """
        Calculate the total number of free seats in the openspace.

        :return: Number of unoccupied seats
        """
        return sum(table.left_capacity() for table in self.tables)

    def is_there_lonely_person(self) -> bool:
        """
        Check if at least one table has exactly one person sitting alone.
        """
        for table in self.tables:
            occupied = [seat for seat in table.seats if not seat.free]
            if len(occupied) == 1:
                return True
        return False

    def eliminate_lonely_tables(self) -> None:
        """
        Redistribute individuals sitting alone to other tables with free seats.
        Ensures no one is left sitting alone.
        """
        lonely_tables = []
        receiving_tables = []

        for table in self.tables:
            occupied = [seat for seat in table.seats if not seat.free]
            free = [seat for seat in table.seats if seat.free]

            if len(occupied) == 1:
                lonely_tables.append((table, occupied[0]))  # table + lone seat
            elif len(free) >= 1:
                receiving_tables.append(table)

        for _, lonely_seat in lonely_tables:
            lonely_person = lonely_seat.occupant

            for target_table in receiving_tables:
                for seat in target_table.seats:
                    if seat.free:
                        # Reassign person
                        seat.occupant = lonely_person
                        seat.free = False

                        # Free old seat
                        lonely_seat.occupant = None
                        lonely_seat.free = True

                        print(f"{lonely_person} was moved from a lonely table to a new table.")
                        break
                else:
                    continue
                break



    def __str__(self) -> str:
        return f"Openspace with {self.number_of_tables} tables"
