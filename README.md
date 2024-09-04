# Functions-to-Script
Turns a series of Python functions into a runnable script with a command line gui

Usage:
To run a script:
`python3 scripter.py test.py`
To get the script:
` python3 scripter.py test.py -s`
The code will be in a file called `scripterRun.py`

Example functions are in the `test.py` file. 
Script functions must not have any parameters or else it will not be considered as a script function.

To add a title/description to a selection in the gui, underneath each function, add a docstring with the desired description.
