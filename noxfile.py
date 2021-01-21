"""Nox test file."""
import tempfile


import nox


nox.options.sessions = "lint", "tests"
locations = "src", "tests", "noxfile.py"
python_latest = "3.9"
python_range = ["3.9", "3.8"]


def install_with_constraints(session, *args, **kwargs):
    """Install environment with restraints."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


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
    session.install("flake8", "flake8-black", "flake8-bugbear", "flake8-import-order")
    session.run("flake8", *args)


@nox.session(python=python_latest)
def black(session):
    """Code formatting with black."""
    args = session.posargs or locations
    session.install("black")
    session.run("black", *args)


@nox.session(python=python_range)
def mypy(session):
    """Type checking."""
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)
