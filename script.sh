# Check Python Version
python_version=$(python3 --version 2>&1) 

if [[ $python_version == *"Python 3."* ]] && [[ $(python3 -c 'import sys; print(sys.version_info >= (3, 6))') == "True" ]]; then
    echo "Python 3.6 or newer is installed: $python_version"
else
    echo "Error: Python 3.6 or newer is not installed. Please install it."
    exit 1 
fi

# Create and Activate Virtual Environment
venv_name=".venv"

if [[ -d $venv_name ]]; then
    echo "Virtual environment '$venv_name' already exists."
else
    python3 -m venv $venv_name
    echo "Virtual environment '$venv_name' created."
fi

source $venv_name/bin/activate

# Run Python Program
python_script="main.py"

if [[ -f $python_script ]]; then
    python $python_script
else
    echo "Error: Python script '$python_script' not found."
    exit 1
fi