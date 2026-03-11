from hello import main


def test_hello(capsys) -> None:
    main()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
