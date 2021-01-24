"""Nox test file."""
import tempfile
from typing import Any


import nox
from nox.sessions import Session


nox.options.sessions = "lint", "mypy", "tests"
locations = "src", "tests", "noxfile.py"
python_latest = "3.9"
python_range = ["3.9", "3.8"]
package = "scatterbrain"


def install_with_constraints(session: Session, *args: str, **kwargs: Any) -> None:
    """Install environment with restraints."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=python_latest)
def black(session: Session) -> None:
    """Code formatting with black."""
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python=python_range)
def lint(session: Session) -> None:
    """Linting for code in locations tuple."""
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-annotations",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-docstrings",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python=python_range)
def tests(session: Session) -> None:
    """Run pytests for each python version."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session, "coverage[toml]", "pytest", "pytest-cov", "pytest-mock"
    )
    session.run("pytest", *args)


@nox.session(python=python_latest)
def safety(session: Session) -> None:
    """Dependency checking."""
    with tempfile.NamedTemporaryFile() as requirements:
        session.run(
            "poetry",
            "export",
            "--dev",
            "--format=requirements.txt",
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        install_with_constraints(session, "safety")
        session.run("safety", "check", f"--file={requirements.name}", "--full-report")


@nox.session(python=python_range)
def mypy(session: Session) -> None:
    """Type checking."""
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)


@nox.session(python=python_range)
def typeguard(session: Session) -> None:
    """Run time type checking."""
    args = session.posargs or ["-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(session, "pytest", "pytest-mock", "typeguard")
    session.run("pytest", f"--typeguard-packages={package}", *args)
