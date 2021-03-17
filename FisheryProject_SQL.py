import mysql.connector, csv

conn = mysql.connector.Connect(host='localhost', user='root', password='', database='Fishing_Team')
cursor = conn.cursor()
print(f'MySQL database version connected to is {conn.get_server_info()}')


def create_db():
    cursor.execute("CREATE DATABASE IF NOT EXISTS Fishing_Team")
    print("Database successfully created")


create_db()

print("\n================================= RUN THESE QUERIES TO CREATE TABLES ======================================\n")


def create_boat_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Boat("
                   "Boat_id INT UNIQUE,"
                   "Boat_Name VARCHAR(25),"
                   "Boat_Size DECIMAL(10, 2),"
                   "Boat_Length DECIMAL(10, 2),"
                   "Station_id VARCHAR(10),"
                   "Boat_Capacity INT,"
                   "Fishing TEXT)")
    print("Boat table successfully created!")


create_boat_table()


def create_fishermen_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Fishermen("
                   "Fisherman_id VARCHAR(10) UNIQUE,"
                   "Fisherman_Name VARCHAR(40),"
                   "Boat_id INT,"
                   "Phone_Number VARCHAR(20),"
                   "Email_Address VARCHAR(40),"
                   "Age INT,"
                   "FOREIGN KEY(Boat_id) REFERENCES Boat(Boat_id))")
    print("Fishermen table successfully created!")


create_fishermen_table()


def create_owners_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS Owners("
                   "Owner_id INT UNIQUE,"
                   "Owner_Name TEXT,"
                   "Boat_id INT UNIQUE,"
                   "Phone_Number VARCHAR(15),"
                   "Email_Address VARCHAR(30),"
                   "FOREIGN KEY(Boat_id) REFERENCES Boat(Boat_id))")
    print('Owners table successfully created!')


create_owners_table()


def create_station_id():
    cursor.execute("CREATE TABLE IF NOT EXISTS Station("
                   "Station_id INT,"
                   "Station_Name TEXT,"
                   "Address VARCHAR(30),"
                   "Boat_id INT,"
                   "FOREIGN KEY(Boat_id) REFERENCES Boat(Boat_id))")
    print("Station table successfully created!")


create_station_id()

print("\n============================== RUN THESE QUERIES TO INSERT DATA TABLES ====================================\n")


def insert_into_boat():
    with open('Boat.csv', 'r') as file:
        next(file)
        for rows in file:
            cursor.execute("INSERT INTO Boat VALUES(%s,%s,%s,%s,%s,%s,%s)", rows.split(','))
        print("Values entered into boat table successfully!")


insert_into_boat()
conn.commit()


def insert_into_fishermen():
    with open('Fishermen.csv', 'r') as file:
        next(file)
        for rows in file:
            cursor.execute("INSERT INTO Fishermen VALUES(%s,%s,%s,%s,%s,%s)", rows.split(','))
        print("Values entered into fishermen table successfully!")


insert_into_fishermen()
conn.commit()


def insert_into_owners():
    with open('Boat_Owners.csv', 'r') as file:
        next(file)
        for rows in file:
            cursor.execute("INSERT INTO Owners VALUES(%s,%s,%s,%s,%s)", rows.split(','))
        print("Values entered into owner table successfully!")


insert_into_owners()
conn.commit()


def insert_into_station():
    with open('Boat_Station.csv', 'r') as file:
        next(file)
        for rows in file:
            cursor.execute("INSERT INTO Station VALUES(%s,%s,%s,%s)", rows.split(','))
        print("Values entered into station table successfully!")


insert_into_station()
conn.commit()


print("\n============================================ JOIN TABLES ==================================================\n")
cursor.execute("SELECT * FROM Boat "
               "JOIN Fishermen ON Boat.Boat_id = Fishermen.Boat_id "
               "JOIN Station ON Station.Boat_id = Fishermen.Boat_id JOIN Owners ON Owners.Boat_id = Station.Boat_id")
query = cursor.fetchall()
for vals in query:
    print(vals)
