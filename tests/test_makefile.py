from pathlib import Path


def test_makefile_exists() -> None:
    makefile = Path(__file__).parent.parent / "Makefile"
    assert makefile.exists()


def test_makefile_has_targets() -> None:
    makefile = Path(__file__).parent.parent / "Makefile"
    content = makefile.read_text()
    for target in ["test", "lint", "clean"]:
        assert f"{target}:" in content
