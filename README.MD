# MyEasySQL

MyEasySQL is a simple Python library to interact with MySQL databases. It provides functions to connect to a database, execute queries, and retrieve data from specific columns or cells.

## Installation

To install myeasysql, run:

```bash
pip install myeasysql
```

## Usage

### Connecting to the Database

Use the `connect` function to establish a connection to the MySQL database:

```python
import myeasysql as sql

cnx = sql.connect('your_host', 'your_user', 'your_password', 'your_database')
```

### Executing a Command

Use the `command` function to execute a query and fetch results:

```python
result = sql.command(cnx, 'your_command')
print(result)
```

### Executing a Raw Command

Use the `rawCommand` function to execute a query and fetch unformatted results:

```python
raw_result = sql.rawCommand(cnx, 'your_command')
print(raw_result)
```

### Retrieving a Column

Use the `getColumn` function to retrieve all values from a specific column in a table:

```python
column_data = sql.getColumn(cnx, 'your_table', 'your_column')
print(column_data)
```

### Retrieving a Cell

Use the `getCell` function to retrieve a specific cell value from a table:

```python
cell_value = sql.getCell(cnx, 'your_table', 'your_column', rowIndex)
print(cell_value)
```

### Retrieving a Row

Use the `getRow` function to retrieve all values from a specific row in a table:

```python
row_data = sql.getRow(cnx, 'your_table', rowIndex)
print(row_data)
```

### Checking if a Number is Even

Use the `isEven` function to check if a number is even:

```python
print(sql.isEven(4))  # Outputs: True
print(sql.isEven(5))  # Outputs: False
```

### Retrieving the Length of a Table

Use the `getLength` function to get the number of rows in a table:

```python
table_length = sql.getLength(cnx, 'your_table')
print(table_length)
```

## Functions

- `connect(host, user, password, database)`: Connects to the MySQL database.
- `command(cnx, query)`: Executes a query and returns the formatted results.
- `rawCommand(cnx, query)`: Executes a query and returns unformatted results.
- `getColumn(cnx, table, column)`: Retrieves all values from a specific column.
- `getCell(cnx, table, column, rowIndex)`: Retrieves a specific cell value from a table.
- `getRow(cnx, table, rowIndex)`: Retrieves all values from a specific row in a table.
- `getLength(cnx, table)`: Retrieves the number of rows in a table.
- `isEven(n)`: Returns `True` if the number is even, otherwise `False`.
