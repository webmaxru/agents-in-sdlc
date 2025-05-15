# Endpoint creation guidelines

## Endpoint notes

- Endpoints are created in Flask using blueprints
- Create a centralized function for accessing data
- All endpoints require tests
    - Tests must use mock objects rather than real database calls
    - Use dictionaries rather than classes for the mocked data
    - Use the `unittest` module for testing
    - All tests must pass

## Project notes

- The Python virtual environment is located in the root of the project in a **venv** folder
- A script is provided to run tests at `scripts/run-server-tests.sh`
- Register all blueprints in `server/app.py`

## Prototype files

- [Endpoint blueprint](server/routes/games.py)
- [Tests blueprint](server/tests/test_games.py)
