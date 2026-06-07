# Useful Commands

Run these from a project folder unless noted otherwise.

## Activate the virtual environment

From the project root:

```bash
source .venv/bin/activate
```

## Run a project

From inside a project folder (for example `01_file_processing/s01_p001_add_date_to_filenames/`):

```bash
python main.py
```

## Run tests

From inside a project folder:

```bash
python -m pytest
```

Run a single test file:

```bash
python -m pytest tests/test_main.py
```

## Install project dependencies

From inside a project folder, after adding packages to `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Create a new project from the template

From the project root, copy the template into a section folder and rename it:

```bash
cp -R 00_course_admin/PROJECT_TEMPLATE/ 01_file_processing/s01_p021_my_new_project
```

Then update placeholders in `README.md` and `main.py`.

## Check Python syntax

From inside a project folder:

```bash
python -m py_compile main.py tests/test_main.py
```

## Git basics

From the project root:

```bash
git status
git add .
git commit -m "Describe your change"
```

## Notes

-
