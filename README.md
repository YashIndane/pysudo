![](https://img.shields.io/badge/license-MIT-yellowgreen)
![](https://img.shields.io/badge/python-3-red)

# pysudo


# Installation Instructions
use pip or pip3 to install the library.
```
pip install pysudo
```

## Importing

```
from pysudo import solve
```

## Example of usage:

```
problem = [[6 , 7 , 0 , 0 , 0 , 0 , 0 , 0 , 2],
           [0 , 0 , 1 , 7 , 9 , 0 , 0 , 3 , 0],
           [0 , 5 , 0 , 0 , 6 , 2 , 0 , 0 , 0],
           [0 , 0 , 0 , 0 , 0 , 0 , 0 , 2 , 5],
           [0 , 0 , 0 , 3 , 0 , 8 , 0 , 0 , 0],
           [2 , 4 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
           [0 , 0 , 0 , 1 , 3 , 0 , 0 , 5 , 0],
           [0 , 8 , 0 , 0 , 5 , 7 , 1 , 0 , 0],
           [5 , 0 , 0 , 0 , 0 , 0 , 0 , 9 , 6]]

solved = solve(problem)

```

The empty cells in the Sudoku puzzle are to be filled by 0.

`solved` is an array having 9 arrays of row inside it representing the complete solved puzzle.

To visualize output use :

```
for rows in solved :
  print(rows)
```

### Output

```
[6, 7, 9, 4, 1, 3, 5, 8, 2]
[8, 2, 1, 7, 9, 5, 6, 3, 4]
[3, 5, 4, 8, 6, 2, 9, 7, 1]
[7, 3, 6, 9, 4, 1, 8, 2, 5]
[1, 9, 5, 3, 2, 8, 4, 6, 7]
[2, 4, 8, 5, 7, 6, 3, 1, 9]
[4, 6, 7, 1, 3, 9, 2, 5, 8]
[9, 8, 2, 6, 5, 7, 1, 4, 3]
[5, 1, 3, 2, 8, 4, 7, 9, 6]
```
