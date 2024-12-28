import mysql.connector

def isEven(n):
    if n % 2 == 0:
        return True
    else:
        return False

def connect(host, user, password, database):
    return mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )

def command(cnx, query):
    cursor = cnx.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cnx.commit()
    formatted_results = []
    for row in results:
        row = str(row)
        row = row.replace("(", "")
        row = row.replace(")", "")
        row = row.replace("'", "")
        row = row.replace('"', "")
        formatted_results.append(row)
    cursor.close()
    return formatted_results

def rawCommand(cnx, query):
    cursor = cnx.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cnx.commit()
    cursor.close()
    return results

def getColumn(cnx, table, column):
    count = getLength(cnx, table)
    data = []

    for name in range(count):
        temp = command(cnx, "SELECT %s from %s limit %d, 1" % (column, table, name))
        if temp:
            data.append(temp[0])

    data = [item for item in data if item not in [None, "Non"]]
    return data

def getCell(cnx, table, column, rowIndex):
    result = getColumn(cnx, table, column)
    result = str(result[rowIndex - 1])
    return result.replace(",", "")

def getRow(cnx, table, rowIndex):
    temp = command(cnx, "SELECT * FROM %s LIMIT 1 OFFSET %d" % (table, rowIndex))
    temp = temp[0].split(", ")
    return temp

def getLength(cnx, table):
    count = command(cnx, "SELECT count(*) from %s" % (table))
    count = count[0].replace(",", "")
    return int(count)