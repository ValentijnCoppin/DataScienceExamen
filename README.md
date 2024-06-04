# Creating the virtual environment
## install Poetry
```bash
pip install poetry
```
## create new a poetry project
Not needed if you manually create a project or want to run an existing project
```bash
poetry new <your_project_name>
```
## add a .venv directory to the project
poetry will write the dependencies in the .venv directory as a standard
Not needed if .venv directory already exists
```bash
mkdir .venv
```
if this command cannot be run in a powershell terminal, you can run powershell as administrator or try it via a command prompt terminal (cmd)
## add dependencies to the project
If you want to add a dependency to the project
```bash
poetry add <package-name>
```
## installing dependencies
```bash
poetry install --no-root
```

## Activating the virtual environment
```bash
.venv\Scripts\activate
```

# Using the notebooks
The solutions can be found in "notebooks/notebook.ipynb"

When opening the notebook, always first "Run all" the cells in order.
This loads the data and processed it in the correct order. 

Afterwards you may re-run specific cells if you like.

## GitHUB repository: https://github.com/ValentijnCoppin/DataScienceExamen