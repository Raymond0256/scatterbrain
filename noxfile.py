"""Nox test file."""
import nox


locations = "src", "tests", "noxfile.py"


@nox.session(python=["3.9", "3.8", "3.7", "3.6"])
def tests(session):
    """Run pytests for each python version."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)


@nox.session(python=["3.9", "3.8", "3.7", "3.6"])
def lint(session):
    """Linting for code in locations tuple."""
    args = session.posargs or locations
    session.install("flake8")
    session.run("flake8", *args)
