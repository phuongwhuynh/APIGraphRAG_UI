# UI_exp Project

This project provides a UI for exploring OpenAPI traces and includes API endpoints, core logic, schemas, and services.

## Project Structure

- `openapi_trace_ui/` - UI for OpenAPI trace visualization
  - `templates/` - Jinja2 HTML templates
  - `utils/` - Helper functions
- `pyproject.toml` - Project dependencies and configuration

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd UI_exp
```

### 2. Install Dependencies and Set Up Environment (with Poetry)

This project uses [Poetry](https://python-poetry.org/) for dependency and environment management. Poetry automatically creates and manages a virtual environment for the project.

```bash
poetry install
```

To activate the Poetry-managed virtual environment, run:

```bash
poetry shell

```

### 3. Configure Environment Variables

```bash
cp .env.example .env
```

Then edit .env to set the correct values for your environment

### 4. Run the Application

Run the application using Poetry:

```bash
poetry run uvicorn openapi_trace_ui.server:app --reload
```

or

```bash
make run-ui
```

- The app will be available at `http://127.0.0.1:8000/` by default.

#### If using another entry point, adjust the command accordingly.

## Additional Notes

- Ensure Python 3.12+ is installed.
