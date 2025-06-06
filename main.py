import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from utils.file_utils import load_and_create_excel
from utils.openspace import Openspace

# === Define color codes ===
BLUE = "\033[94m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def main() -> None:
    # Clear terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')

    # File paths and config
    input_file = "problem-statement/collegues.csv"
    output_file = "data/output.csv"
    excel_file = "data/colleagues.xlsx"
    tables = 6
    seats_per_table = 4

    # Load names
    names = load_and_create_excel(input_file, excel_file)
    print(f"\n{BLUE}>>> Loaded {len(names)} names from: {input_file}{RESET}")
    print(f"{BLUE}>>> Excel file created at: {excel_file}{RESET}\n")

    # Set up the room
    room = Openspace(tables, seats_per_table)
    print(f"{BLUE}>>> Assigning colleagues to seats...{RESET}\n")
    room.organize(names)

    # Display and export
    print(f"{BLUE}>>> Displaying seating arrangement:{RESET}\n")
    room.display()

    print(f"\n{BLUE}>>> Saving seating plan to: {output_file}{RESET}\n")
    room.store(output_file)

    print(f"{GREEN}>>> Program completed successfully.{RESET}\n")

if __name__ == "__main__":
    main()
