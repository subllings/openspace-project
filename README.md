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

