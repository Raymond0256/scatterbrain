"""Nox test file."""
import tempfile


import nox


nox.options.sessions = "lint", "mypy", "tests"
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
            "--without-hashes",
            f"--output={requirements.name}",
            external=True,
        )
        session.install(f"--constraint={requirements.name}", *args, **kwargs)


@nox.session(python=python_range)
def tests(session):
    """Run pytests for each python version."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", "--no-dev", external=True)
    install_with_constraints(
        session, "coverage[toml]", "pytest", "pytest-cov", "pytest-mock"
    )
    session.run("pytest", *args)


@nox.session(python=python_range)
def lint(session):
    """Linting for code in locations tuple."""
    args = session.posargs or locations
    install_with_constraints(
        session,
        "flake8",
        "flake8-bandit",
        "flake8-black",
        "flake8-bugbear",
        "flake8-import-order",
    )
    session.run("flake8", *args)


@nox.session(python=python_latest)
def black(session):
    """Code formatting with black."""
    args = session.posargs or locations
    install_with_constraints(session, "black")
    session.run("black", *args)


@nox.session(python=python_latest)
def safety(session):
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
def mypy(session):
    """Type checking."""
    args = session.posargs or locations
    install_with_constraints(session, "mypy")
    session.run("mypy", *args)
