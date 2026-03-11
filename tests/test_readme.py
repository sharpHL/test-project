from pathlib import Path


def test_readme_has_python_badge() -> None:
    readme = Path(__file__).parent.parent / "README.md"
    content = readme.read_text()
    assert "https://img.shields.io/badge/python" in content
