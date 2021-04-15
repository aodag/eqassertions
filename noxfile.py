import nox

package = "eqassertions"

nox.options.sessions = ["test"]


@nox.session
def test(session: nox.Session):
    session.install("-e.[testing]")
    session.run("pytest", "tests", f"--cov={package}", "--cov-report=term-missing")


@nox.session
def pack(session: nox.Session):
    session.install("build")
    session.run("python", "-m", "build", ".")
