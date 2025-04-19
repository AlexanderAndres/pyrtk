# PyRTK - Python REST Toolkit

PyRTK is a developer-friendly CLI and framework for building structured, scalable REST APIs and microservices in Python. It brings modularity, best practices and FastAPI power under one unified command-line workflow.

---

## Why PyRTK?

Developing microservices in Python can often lead to disorganized projects, duplicated boilerplate, and a lack of standardization. PyRTK solves that by:

- Providing opinionated folder structures for APIs and microservices
- Scaffolding CRUD components instantly with `pyrtk generate`
- Automating common tasks like router registration
- Promoting modular, maintainable codebases

---

## Features

- 🔧 CLI generator for microservices and REST APIs
- ⚙️ CRUD scaffolding (`generate`)
- 🧩 Auto-router registration
- 📦 Built-in FastAPI integration
- 🧼 Project conventions based on best practices

---

## Roadmap

- [x] CLI with `create`, `run`, `generate`
- [x] Auto-register routers in main.py
- [x] Custom project structure per type (`api`, `ms`)
- [ ] Internal build tools (`build`, `release`)
- [ ] VS Code generator extension (maybe?)
- [ ] Plugin system for extensions

---

## Getting Started

### 1. Create a virtual environment

```bash
python3 -m venv pyrtk-env
source pyrtk-env/bin/activate  # On Windows: .\pyrtk-env\Scripts\activate
```

### 2. Install PyRTK

#### For general usage (just to use the CLI):
```bash
pip3 install .
```

#### For development (with test and build tools):
```bash
pip3 install -e ".[dev]"
```

### 3. Verify installation

```bash
pyrtk --help
```
