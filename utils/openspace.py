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



    def __str__(self) -> str:
        return f"Openspace with {self.number_of_tables} tables"
