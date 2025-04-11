# 📦 CHANGELOG

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