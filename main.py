import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from utils.file_utils import create_excel_from_csv, load_colleagues_from_excel, load_config
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
    excel_file = "data/colleagues.xlsx"
    output_file = "data/output.csv"
    config = load_config()
    tables = config["tables"]
    seats_per_table = config["seats_per_table"]

    # Create Excel file from CSV
    create_excel_from_csv(input_file, excel_file)
    print(f"\n{BLUE}>>> Excel file created at: {excel_file}{RESET}")

    # Load names from Excel file
    names = load_colleagues_from_excel(excel_file)
    print(f"{BLUE}>>> Loaded {len(names)} names from: {excel_file}{RESET}\n")

    # Set up the room
    room = Openspace(tables, seats_per_table)
    print(f"{BLUE}>>> Assigning colleagues to seats...{RESET}\n")
    room.organize(names)

    
    # Manage and eliminate lonely persons at tables 
    if room.is_there_lonely_person():
        print(">>> Lonely persons detected. Eliminating lonely tables...\n")
        room.eliminate_lonely_tables()
        print(">>> Re-displaying seating arrangement after elimination:\n")
        room.display()
    else:
        print(">>> No lonely persons detected.\n")

    
    # Display number of remaining seats
    print(f"{BLUE}>>> {room.seats_left()} seats left in the room.{RESET}\n")



    print(f"\n{BLUE}>>> Saving seating plan to: {output_file}{RESET}\n")
    room.store(output_file)

    print(f"{GREEN}>>> Program completed successfully.{RESET}\n")

if __name__ == "__main__":
    main()
