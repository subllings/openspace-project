# !/bin/bash

# chmod +x run-web.sh
# ./run-web.sh

# Activate venv
if [ -f ".venv/Scripts/activate" ]; then
  source .venv/Scripts/activate
elif [ -f ".venv/bin/activate" ]; then
  source .venv/bin/activate
else
  echo "Virtualenv not found"
  exit 1
fi

#export FLASK_APP=user_interface/web/webapp.py
export FLASK_APP=user_interface.webapp
export PYTHONPATH=$(pwd)

flask run