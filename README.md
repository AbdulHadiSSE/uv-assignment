# UV Assignment - PIAIC

**Author:** Abdul Hadi  
**PIAIC Registration:** PIAIC228505

This repository contains two Python applications demonstrating UV package management:

## Projects

### 1. Simple App
- **Location:** `simple-app/`
- **Description:** Basic Python application with OpenAI agents dependency
- **Dependencies:** openai-agents>=0.2.11
- **Python Version:** >=3.13

### 2. Packaged App
- **Location:** `packaged-app/`
- **Description:** Packaged Python application with console script entry points
- **Features:** 
  - Console script commands: `main` and `packaged-app`
  - Displays author information and PIAIC registration
- **Python Version:** >=3.13

## Setup

Each project uses UV for dependency management. Navigate to the respective project directory and run:

```bash
uv sync
```

## Running the Applications

### Simple App
```bash
cd simple-app
uv run python main.py
```

### Packaged App
```bash
cd packaged-app
uv run main
# or
uv run packaged-app
```

## Project Structure
```
uv-assignment/
├── simple-app/
│   ├── main.py
│   ├── pyproject.toml
│   ├── uv.lock
│   └── README.md
├── packaged-app/
│   ├── src/packaged_app/
│   │   ├── __init__.py
│   │   └── main.py
│   ├── pyproject.toml
│   ├── uv.lock
│   └── README.md
└── README.md
```