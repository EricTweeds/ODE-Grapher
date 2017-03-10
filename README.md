# ODE-Grapher
Python Script that creates graphs needed for an ODE's project

## Rules:
- The function must be inside quotation marks
- No need to add y=, just include everything past the equals sign
- Use * for multiplication, / for division, \** for exponent, exp(x) for e^x
- When all the functions for the graph are entered, press enter and leave the final equation blank, the script will interpret this as saying done.
- Up to 8 equations can be entered, it is recomended to cap it at 3 however
- The range of the X-axis is always 0 - 9 since that is the range specified in the project, the range can be changed from within the code
- The math in the script is powered by Numpy so if you are unsure how to enter an equation, check out that library:
https://docs.scipy.org/doc/numpy/reference/routines.math.html

## Example:
y(t) = sin(2t)

enter as:

'sin(2*x)'

Output:

![alt tag](https://github.com/EricTweeds/ODE-Grapher/blob/master/example1.png?raw=true)
