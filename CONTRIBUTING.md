# Contributing to sensitive-word-filter-cn

## Project Status

This is a **personal project**, currently maintained solely by [PerryLink](https://github.com/PerryLink) (novelnexusai@outlook.com). External contributions are welcome but response times may vary.

---

## Reporting Issues

If you find a bug or have a feature request, please [open an issue](https://github.com/PerryLink/sensitive-word-filter-cn/issues) and include:

- A clear description of the problem or request
- Steps to reproduce the issue (for bugs)
- Expected vs. actual behavior
- Your Python version and operating system
- Relevant code snippets or error messages

---

## Development Setup

**Requirements:** Python 3.8+, [Poetry](https://python-poetry.org/)

```bash
# 1. Fork and clone the repository
git clone https://github.com/PerryLink/sensitive-word-filter-cn.git
cd sensitive-word-filter-cn

# 2. Install dependencies (including dev tools)
poetry install

# 3. Activate the virtual environment
poetry shell

# 4. Verify the setup by running tests
pytest tests/ -v
```

---

## Code Style

This project follows [PEP 8](https://peps.python.org/pep-0008/) and uses the following tools:

| Tool | Purpose | Config |
|------|---------|--------|
| [black](https://github.com/psf/black) | Code formatting | `line-length = 100` |
| [ruff](https://github.com/astral-sh/ruff) | Linting | `line-length = 100` |

Before committing, run:

```bash
black src/ tests/
ruff check src/ tests/
```

Key conventions:
- Line length: 100 characters
- Target Python version: 3.8+
- Docstrings: Google style
- Type hints: encouraged for public APIs

---

## Running Tests

```bash
# All tests
pytest tests/ -v

# Unit tests only
pytest tests/test_core.py tests/test_utils.py tests/test_cli.py -v

# Performance benchmarks
pytest tests/test_performance.py --benchmark-only

# With coverage report
pytest tests/ --cov=src/sensitive_word_filter_cn --cov-report=term-missing
```

All tests must pass before submitting a Pull Request.

---

## Submitting a Pull Request

1. **Fork** the repository and create a branch from `main`:

   ```bash
   git checkout -b fix/your-fix-name
   # or
   git checkout -b feat/your-feature-name
   ```

2. **Make your changes**, following the code style above.

3. **Write or update tests** to cover your changes.

4. **Run the full test suite** and ensure everything passes:

   ```bash
   black src/ tests/
   ruff check src/ tests/
   pytest tests/ -v
   ```

5. **Commit** with a clear message:

   ```
   fix: resolve incorrect pinyin matching for multi-character words
   feat: add whitelist support for false-positive reduction
   ```

6. **Open a Pull Request** against the `main` branch. Describe:
   - What the change does
   - Why it is needed
   - How it was tested

---

## License

By contributing, you agree that your contributions will be licensed under the [Apache License 2.0](LICENSE).

Copyright 2026 Chance Dean (novelnexusai@outlook.com)
