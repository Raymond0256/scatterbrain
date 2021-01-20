"""Nox test file."""
import nox


@nox.session(python=["3.9", "3.8", "3.7", "3.6"])
def tests(session):
    """Run pytests for each python version."""
    args = session.posargs or ["--cov", "-m", "not e2e"]
    session.run("poetry", "install", external=True)
    session.run("pytest", *args)
