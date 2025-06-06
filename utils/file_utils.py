import csv
from typing import List

def load_colleagues_from_csv(filepath: str) -> List[str]:
    """
    Read names from a CSV file (one name per line).
    """
    names: List[str] = []

    with open(filepath, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                names.append(row[0].strip())

    return names
