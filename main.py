import pyodbc
#import json
#contraseña = open("my_passwd.json", "r")
#YOUR_PASSWORD = json.load(contraseña) #json es sólo el string de su contraseña.
#contraseña.close()
YOUR_PASSWORD = "Server_123" # CAMBIAR A JSON

# Set up your connection string
server = 'class3-server.database.windows.net'
database = 'class3-database'
username = 'Jesús'
password = YOUR_PASSWORD

# Define the connection string for SQL Server (Azure)
conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={server};'
    f'DATABASE={database};'
    f'UID={username};'
    f'PWD={password}'
)

# Establish the connection
try:
    conn = pyodbc.connect(conn_str)
    print("Connected to the Azure SQL Database successfully!")

except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")