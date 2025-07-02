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

## Future Improvements
Time used: ~7 hours

If I had more time, I would:
- Add executable
- Add more comprehensive tests, covering all edge cases
- Add some user input validations
- Improve error handling
- Add logging
- Add some linter to also run during pull request checks
- Make some fixes: better GUI, "Add New Book" -view showing fields before clicking, longer book names shown better in GUI etc.

## My thoughts about quality as a QA Engineer since 2015
I believe quality begins with simple steps and accumulates over time. It's not just about testing features when they're finished, but also protecting the project from bad practises early on — such as developers pushing directly to main. Having solid unit tests helps ensure that developers don't unecessarily break the code, because fixing issues early is less expensive than discovering them later during QA.