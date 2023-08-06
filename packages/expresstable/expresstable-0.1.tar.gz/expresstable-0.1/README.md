## expresstable

A quick and dirty Python package for creating simple tables. This was created to solve a specific problem, if you're looking for something with more power and customisation you should check out [tabulate](https://pypi.org/project/tabulate/) or [PrettyTable](https://pypi.org/project/PrettyTable/).

#### Quick start
Creating a table is straight forward...
```python
>>> from expresstable import Table
>>> table = Table()
>>> table.add_row(["Name", "Age", "Gender"], header=True)
>>> table.add_row(["Chris", 28, "M"])
>>> table.add_row(["Tara", 25, "F"])
>>> table.add_row(["Ben", 39, "M"])
>>> print(table)

 ----------------------
  Name  | Age | Gender
 ----------------------
  Chris | 28  | M
  Tara  | 25  | F
  Ben   | 39  | M
```
#### Styling

The characters used to display the vertical and horizontal border can be altered by passing the `vborder` and `hborder`keyword argument when creating the table; e.g.

```python
>>> from expresstable import Table

>>> table = Table(vborder=':', hborder='=')
>>> table.add_row(["Name", "Age", "Gender"], header=True)
>>> print(table)

 ======================
  Name  : Age : Gender
 ======================

```

Additionally there are a variety of keyword arguments which can be used to alter the look of the entire table, individual rows, or specific cells.

- `bold` - Display text in bold (boolean, default: `False`)
- `fgcolor` - Color of forground (string, default: `None`)
- `bgcolor` - Color of background (string, default: `None`)
- `dark` - Use a slighty darker variant of the provided fgcolor (boolean, default: `False`)
- `align` - Align text (default: `"left"`, options: `["left", "center", "right"`)

These can be passed to the entire Table:
```python
table = Table(**kwargs)
```
To a specific row:
```python
table = Table()
table.add_row(["cell one", "cell two"], **kwargs)
```
Or to specific cells:
```python
table = Table()
table.add_row(
    [Cell("cell 1", **kwargs), Cell("cell 2", **kwargs)],
    **kwargs)
```
#### Example
```python
from expresstable import Table, Cell

table = Table(align="center")
table.add_row([Cell("Name", align="left"), "Age", "Gender"], header=True)
table.add_row([Cell("Christopher", align="left"), 28, "M"], fgcolor="red")
table.add_row([Cell("Holly", align="left"), 24, "F"], fgcolor="yellow")
table.add_row([Cell("Patrick", align="left"), 26, Cell("M", bold=True, bgcolor="white")], fgcolor="green")
print(table)
```

![Screenshot](https://raw.githubusercontent.com/christopherdavidsmith/expresstable/master/images/screenshot.png)

#### Future
- Add ability to control style of specific columns
- Create table from list of lists
- Add columns to table
#### Changelog
- 0.1 - Initial commit
