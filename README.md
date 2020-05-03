# CS 170 Project
## Dependencies
In our solver, we have the following dependencies:

 - NetworkX
 - Parse (included in skeleton code **`parse.py`**)
 - Utils (included in skeleton code as **`utils.py`**)
 - Sys
 - Os

## Usage
First create a folder called "inputs" in the same directory as **`solver.py`**
An "outputs" folder to store the outputs of **`solver.py`** should also be in the same directory.

To run it on all inputs in the "inputs" folder:
```python
python solver.py
```

To run it on a single input, comment out the last section of code starting from line 93 and uncomment the section from line 81 to line 91.

```python
python solver.py <path_to_input_file>
```
This will out a file called **`output.out`** in the same directory as **`solver.py`**.

