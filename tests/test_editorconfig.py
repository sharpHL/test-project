from pathlib import Path


def test_editorconfig_exists() -> None:
    config = Path(__file__).parent.parent / ".editorconfig"
    assert config.exists()


def test_editorconfig_has_root() -> None:
    config = Path(__file__).parent.parent / ".editorconfig"
    content = config.read_text()
    assert "root = true" in content
