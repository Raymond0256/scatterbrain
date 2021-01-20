"""Nox test file."""
import nox


nox.options.sessions = "lint", "tests"
locations = "src", "tests", "noxfile.py"
python_latest = "3.9"
python_range = ["3.9", "3.8", "3.7", "3.6"]


@nox.session(python=python_range)
def tests(session):
    """Run pytests for each python version."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=python_range)
def lint(session):
    """Linting for code in locations tuple."""
    args = session.posargs or locations
    session.install("flake8", "flake8-black")
    session.run("flake8", *args)


@nox.session(python=python_latest)
def black(session):
    """Code formatting with black."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)
