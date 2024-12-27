# MyEasySQL

MyEasySQL is a simple Python library to interact with MySQL databases. It provides functions to connect to a database, execute queries, and retrieve data from specific columns or cells.

## Installation

To install the required MySQL connector, run:

```bash
pip install mysql-connector-python
```

## Usage

### Connecting to the Database

Use the `connect` function to establish a connection to the MySQL database:

```python
from myeasysql import main

cnx = main.connect(host='your_host', user='your_user', password='your_password', database='your_database')
```

### Executing a Command

Use the `command` function to execute a query and fetch results:

```python
result = main.command(cnx, 'SELECT * FROM your_table')
print(result)
```

### Retrieving a Column

Use the `getColumn` function to retrieve all values from a specific column in a table:

```python
column_data = main.getColumn(cnx, 'your_table', 'your_column')
print(column_data)
```

### Retrieving a Cell

Use the `getCell` function to retrieve a specific cell value from a table:

```python
cell_value = main.getCell(cnx, 'your_table', 'your_column', rowIndex=1)
print(cell_value)
```

## Functions

- `connect(host, user, password, database)`: Connects to the MySQL database.
- `command(cnx, query)`: Executes a query and returns the results.
- `getColumn(cnx, table, column)`: Retrieves all values from a specific column.
- `getCell(cnx, table, column, rowIndex)`: Retrieves a specific cell value from a table.

## License

This project is licensed under the MIT License.
