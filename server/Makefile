env:
	source ./env/bin/activate

install:
	python3 -m venv env && source ./env/bin/activate && pip install -r requirements.txt

server: env
	uvicorn server.main:app --reload
