.PHONY: test lint clean

test:
	python3 -m pytest tests/ -v

lint:
	python3 -m flake8 .

clean:
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type d -name .pytest_cache -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
