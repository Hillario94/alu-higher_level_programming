# Python - Almost a circle

This project reviews Python classes, inheritance, `*args` / `**kwargs`,
JSON serialization, file handling and unit testing.

## Files

- `models/base.py`: `Base` class (id management, JSON and file helpers)
- `models/rectangle.py`: `Rectangle` class inheriting from `Base`
- `models/square.py`: `Square` class inheriting from `Rectangle`
- `tests/test_models/`: unit tests for each class

## Running the tests

    python3 -m unittest discover tests

Single file:

    python3 -m unittest tests/test_models/test_base.py
