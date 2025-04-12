# 📦 CHANGELOG

## [0.1.3] - 2024-04-10
### Added
- `pyrtk generate <name>` command to scaffold full CRUD structure
- Generates: routers/, models/, schemas/, services/ with `__init__.py` and base file
- Automatically registers router in `main.py` after `apply_middlewares(app)`

### Improved
- Developer workflow and structure for rapid scaffolding

## [0.1.2] - 2024-04-10
### Added
- Minimal CLI output during `create`: only progress bars shown, no verbose logs
- Spinner for virtual environment creation and dependency installation
- Clean `install.py` handling for professional UX

### Fixed
- CLI structure now uses `@app.command()` for all top-level commands
- Removed nested `create` command issue
- Corrected main CLI registration to import only callable objects

---

## [0.1.1] - 2024-04-10
### Added
- Modular CLI architecture using Typer (commands split into `cli/` directory)
- Internal logic extracted into `internal/run_logic.py`
- `pyrtk run` command now launches Uvicorn cleanly using the local virtual environment
- Installation support via `pipx`
- Tracking logs without interference from rich spinners

### Fixed
- Fixed: `entry_point` in setup.py now points to `main.py`
- Fixed: Uvicorn logs are now clean and not overwritten by CLI output

---

## [0.1.0] - 2024-04-05
### Added
- Initial prototype of PyRTK CLI
- `pyrtk create` command for scaffolding API and microservice projects
- Basic `pyrtk run` command (non-modular, inline logic)
