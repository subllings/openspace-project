# Openspace Project

## Prerequisites

Before running this project, ensure that Python 3.12.10 is installed on your system.

- You can download Python 3.12.10 from the official website:  
https://www.python.org/downloads/release/python-31210/

- Make sure the `python.exe` path is added to your system environment variables (`PATH`) so it can be accessed via terminal:
-  On Windows, this is typically located at:  
`C:\Users\<YourUserName>\AppData\Local\Programs\Python\Python312\python.exe`

> ⚠️ This project is configured to create a virtual environment using Python 3.12.10. Other versions may lead to compatibility issues.

## Python Environment Setup

This project uses a **virtual environment** to manage Python dependencies in isolation from your system installation.  
This is done using the `.venv/` folder, which contains a local version of Python and all required packages for the project.

> **Why use a virtual environment?**  
> It ensures:
> - Your project runs with the exact versions of libraries it needs.
> - No conflicts with other Python projects or your system installation.
> - Clean and reproducible development environments.

### Step-by-step setup

To initialize the Python environment for this project, follow these steps:

1. **Open a Bash-compatible terminal**  
   Use Git Bash (recommended on Windows) or WSL if you're on Linux/macOS.

2. **Make the setup script executable**  
   Run the following command once to make the script executable:
   ```bash
   chmod +x setup-env.sh
   ```

3. **Run the setup script**
   ```bash
   ./setup-env.sh
   ```

This script will:
- Remove any existing `.venv/` folder.
- Create a new virtual environment using **Python 3.12.10**.
- Automatically activate the environment.
- Upgrade `pip`.
- Install all required packages from `requirements.txt`.
- Create a new `.venv/` folder in the project root to isolate dependencies.

> After those steps, your environment is fully set up and ready for development or testing.

## Running Unit Tests

Once the Python environment is set up, you can run the test suite to validate the project components.

1. **Make the setup script executable** 
    ```bash
    chmod +x run-test.sh
    ```

2. **Run the setup script**
   ```bash
   ./run-test.sh
   ```

This script will:
- Activate the virtual environment.
- Run all unit tests using pytest.
- Display test coverage statistics.
- Highlight which parts of the code are not yet covered by tests.
- Exit with an error if any test fails.
  
> This ensures your project stays robust, maintainable, and production-ready.

### Using the code

1. **Launch**
   
   Open git bash terminal in VSC and type:

      chmod +x run-main.sh && ./run-main.sh
      ./run-main.sh

   Running this shell script sets the virtual environment
   and launches the main script: main.py.

2. **Workflow, input and output**

   -  The code begins with downloading a list of students from an Excel file
   stored in the data folder: colleagues.xlsx.

   - The list of students is used to randomly assign tables and seats.

   - A check is done to see if there are tables with only one person assigned.
   In this case a review of the tables with at least one person is done and the person is re-assigned to that table.
  
   - The number of free seats left is outputted on the screen.
  
   - The assigned table namuber, seat number, and person's name are written
      to a csv file output.csv in the data directory.    

3. **Algorithm for assigning seats**

   When script main.py initiates an Openspace class object, the constructor
   of the latter first creates a list of table objects, each table getting capacity parameter as input (4 chairs default).
   
   The principal method of the Openspace class - organize -
   receives a list of students (extracted from the Excel file).
   It then reshuffles the student list simulating random order in which students arrive. After that for each student from the reshuffled list it reshuffles the table list as well, assigning then the first available table.
   The table is considred available when there are free seats.

   After the first assignment, methods is_there_lonely_person
   and eliminate_lonely_tables of the Openspace are run that
   reassign people whol were left alone at the table to other available tables.
   
   If all tables are occupied, the student does not get a seat assignment and is added to the "unassigned list" that is printed on screen at the end of the execution of the code.
   
   The assignment of the seat at the table is done by calling assign_seat method of the Table's class, which in turn calls method set_occupant in the Seat's class. The seat numbers are not shuffled - they are assigned for a given table in the order from 1 to 4.

4. **Configurable parameters**

   You can change the number of the tables and the seats, as well as the names of the input csv, intermediate xlsx, and output files in the file: config.json.



