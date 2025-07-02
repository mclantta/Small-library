# Small-library
Small Python program for storing books

## How to run the program
TBD (needs executable first)

## How to continue development (Linux and Mac Terminal)
Note: project was done in macOS, but all of the terminal commands should be the same in Linux

Clone project to your own computer.
Go to a project folder. Create there your own virtual environment for example with a command:
```
python3 -m venv "venv"
```

Open created virtual env:
```
source venv/bin/activate
```

Install all needed packages in virtual env from requirements.txt -file:
```
python -m pip install -r requirements.txt
```

Run program in virtual env
```
python src/main.py library.txt
```

## Run tests
```
pytest
```