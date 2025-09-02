.PHONY: install run dev test

install:
	pip install -r requirements.txt

run:
	uvicorn main:app

dev:
	uvicorn main:app --reload

test:
	pytest