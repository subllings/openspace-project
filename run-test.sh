#!/bin/bash

# Make this script executable: chmod +x run-test.sh
# Run it with: ./run-test.sh

clear

# ------------------------------------------
# Run all unit tests for the Open Space app
# ------------------------------------------

# Define colors
BLUE_BG="\033[44m"
GREEN_BG="\033[42m"
RED_BG="\033[41m"
WHITE_TEXT="\033[97m"
BLACK_TEXT="\033[30m"
RESET="\033[0m"

# Utility print functions
print_blue() {
  echo ""
  echo -e " ${BLUE_BG}${BLACK_TEXT}$1${RESET}"
  echo ""
}

print_green() {
  echo ""
  echo -e " ${GREEN_BG}${WHITE_TEXT}$1${RESET}"
  echo ""
}

print_red() {
  echo ""
  echo -e " ${RED_BG}${WHITE_TEXT}$1${RESET}"
  echo ""
}

# Stop on first error
set -e

# Activate virtual environment
print_blue ">>> Activate virtual environment..."
if [ -f ".venv/Scripts/activate" ]; then
  source .venv/Scripts/activate
elif [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
else
  print_red ">>> Could not find virtual environment activation '.venv/Scripts/activate' script."
  exit 1
fi

print_blue ">>> Running tests..."
export PYTHONPATH=$(pwd | sed 's/\\/\\\\/g')
pytest
TEST_RESULT=$?

print_blue ">>> Test coverage..."
pytest --cov=models tests/

print_blue ">>> Files with missing coverage..."
pytest --cov=models --cov-report=term-missing tests/

if [ $TEST_RESULT -eq 0 ]; then
  print_green ">>> All tests passed successfully"
else
  print_red ">>> One or more tests failed"
fi
