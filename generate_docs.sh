# Create and Activate Virtual Environment
venv_name=".venv"

if [[ -d $venv_name ]]; then
    echo "Virtual environment '$venv_name' already exists."
else
    python3 -m venv $venv_name
    echo "Virtual environment '$venv_name' created."
fi

source $venv_name/bin/activate
pip install pdoc
pdoc *.py -d google -o documentation