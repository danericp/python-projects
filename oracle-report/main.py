import cx_Oracle

# Replace these values with your actual Oracle database credentials
username = 'your_username'
password = 'your_password'
dsn = 'your_oracle_dsn'  # Oracle Data Source Name (TNS)

try:
    # Establish a connection to the Oracle database
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Example query: Replace this with your SQL query
    sql_query = "SELECT * FROM your_table"

    # Execute the query
    cursor.execute(sql_query)

    # Fetch and print the results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    connection.close()

except cx_Oracle.Error as error:
    print("Error connecting to Oracle database:", error)
