import csv
import os
import pandas as pd
from typing import List


def load_and_create_excel(filepath_csv: str, output_xlsx: str = "data/colleagues.xlsx") -> List[str]:
    """
    Load colleague names from a CSV file and create an Excel file in the 'data' folder.

    :param filepath_csv: Path to the CSV file (source)
    :param output_xlsx: Path where the Excel file will be saved
    :return: List of names
    """
    names: List[str] = []

    with open(filepath_csv, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if row:
                names.append(row[0].strip())

    # Save Excel file
    df = pd.DataFrame(names, columns=["Name"])
    os.makedirs(os.path.dirname(output_xlsx), exist_ok=True)
    df.to_excel(output_xlsx, index=False)

    return names

