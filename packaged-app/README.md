# Packaged App

**Author:** Abdul Hadi  
**PIAIC Registration:** PIAIC228505

A packaged Python application with console script entry points that displays author information.

## Features
- Packaged Python application structure
- Console script entry points
- UV build system integration
- Python 3.13+ compatible

## Setup

1. Install dependencies:
```bash
uv sync
```

2. Run the application using console scripts:
```bash
uv run main
# or
uv run packaged-app
```

## Console Scripts
- `main`: Executes the greet function
- `packaged-app`: Alternative entry point

## Project Structure
```
packaged-app/
├── src/
│   └── packaged_app/
│       ├── __init__.py
│       └── main.py
├── pyproject.toml
├── uv.lock
└── README.md
```

## App Output

![App Output](screenshot.jpg)
