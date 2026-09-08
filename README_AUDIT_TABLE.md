# README audit table

| Claim made in README | True? | Evidence or correction made |
|---|---|---|
| Requires pip install -r requirements.txt | No | No `requirements.txt` exists; standard library only. Delete this line if present. |
| Repository contains beginner-friendly Python programs for a class. | Yes | Files `hello_world.py`, `fibonacci.py`, and `factorial.py` are present and focused on programming basics. |
| No external dependencies are required; standard library only. | Yes | README states standard library usage, and no dependency file is present. |
| No license is currently specified in this repository. | Yes | No `LICENSE` file is present in the repository root. |
| `hello_world.py` prints a basic greeting. | Yes | Running `python hello_world.py` outputs `Hello, world!`. |
| `fibonacci.py` generates the first 10 Fibonacci numbers in sample command. | Yes | Running `python fibonacci.py` outputs `The first 10 Fibonacci numbers are: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`. |
| `factorial.py` can be run as shown and produces sample output. | No | Running `python factorial.py` currently fails with `SyntaxError` at line 1 due to `//` comment syntax. |
