import nox

package = "eqassertions"

@nox.session
def test(session: nox.Session):
    session.install("-e.[testing]")
    session.run("pytest", "tests", f"--cov={package}", "--cov-report=term-missing")
