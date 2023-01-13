## Overview

This is a repository with the implementation of a module in Python, which aims to read a JSON file and create the full dependency graph.

Implemented by: Agata Kaczmarek

## How to run?

To run the module:
```sh
python -m dep_graph
```
To run the tests for the module, you have to install `pytest` from the `requirements.txt` file or with:
```sh
pip install -U pytest
```
and run tests with:
```sh
pytest
```

## Solution description

The created program reads a JSON file from a fixed location and creates a full dependency graph, based on the content of that file. To do so, it uses only built-in Python functions. Function reading and converting JSON is called json_to_graph_function, stored in `json_to_graph.py`. To correctly return the names of the dependencies the nested function `recursively_add_names` is implemented inside `json_to_graph_function`.

## Task description

We would like you to write a small Python program following best Python standards and coding practices.

This program must read a JSON file from a fixed filesystem location, e.g. `/tmp/deps.json`, containing a list of packages and their dependencies. In this JSON file, a key represents a package name, and the value is a list of dependencies (package names) for that key:

```json
{
    "pkg1": ["pkg2", "pkg3"],
    "pkg2": ["pkg3"],
    "pkg3": []
}
```

Traverse the dependencies loaded from the JSON file and reconstruct the full dependency graph. For the input above, the full graph would be the following:

```sh
- pkg1
  - pkg2
    - pkg3
  - pkg3
- pkg2
  - pkg3
- pkg3
```

The program should be a valid Python package or module named `dep_graph` and be runnable with `python -m dep_graph` command. Running this command should print the graph to `stdout`. The format in which it prints is not important.

The `dep_graph` module should contain a function that takes a filename as an input and returns an object representing the fully resolved graph. Please provide a test case that validates this function. Use any testing framework of your choice.

Use any appropriate tools from the standard library to help with your implementation, and write the code such that it is as readable and maintainable as possible, e.g. docstrings, type hints, comments, etc. Organize the code in the file hierarchy that is the most appropriate for such package or module.

