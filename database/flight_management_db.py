import sqlite3
from database.seed_data.data import seed_query_data

DATABASE_FILE = "database/flight_management_store.db"

def get_db_connection():
    return sqlite3.connect(DATABASE_FILE); 

def create_tables(cursor: sqlite3.Cursor): 
    create_queries = [
        """CREATE TABLE IF NOT EXISTS destinations (
            DestinationID INTEGER PRIMARY KEY, 
            AirportName VARCHAR(255) NOT NULL, 
            AirportCode VARCHAR(10) NOT NULL, 
            City VARCHAR(255) NOT NULL, 
            Country VARCHAR(255) NOT NULL
        )""",
        """CREATE TABLE IF NOT EXISTS pilots (
            PilotID INTEGER PRIMARY KEY, 
            FirstName VARCHAR(255) NOT NULL, 
            LastName VARCHAR(255) NOT NULL, 
            DOB DATE, 
            LicenceNumber VARCHAR(10) NOT NULL)""",
        """CREATE TABLE IF NOT EXISTS flights (
            FlightID INTEGER PRIMARY KEY, 
            FlightNumber VARCHAR(10) NOT NULL, 
            DepartureDate DATE NOT NULL, 
            DepartureTime VARCHAR(5) NOT NULL, 
            ArrivalTime VARCHAR(5) NOT NULL, 
            Status VARCHAR(10) NOT NULL, 
            OriginID INTEGER NOT NULL, 
            DestinationID INTEGER NOT NULL, 
            FOREIGN KEY (OriginID) REFERENCES Destinations(DestinationID), 
            FOREIGN KEY (DestinationID) REFERENCES Destinations(DestinationID)
        )""",
        """CREATE TABLE IF NOT EXISTS schedules (
            FlightID INTEGER, PilotID INTEGER, 
            AssignedDate VARCHAR(10) NOT NULL, 
            PRIMARY KEY (FlightID, PilotID), 
            FOREIGN KEY (FlightID) REFERENCES Flights(FlightID), 
            FOREIGN KEY (PilotID) REFERENCES Pilots(PilotID)
        )"""
    ]


    for create_query in create_queries: 
        cursor.execute(create_query)

    print("Databa init completed")

def seed_data(conn: sqlite3.Connection, cursor: sqlite3.Cursor):
    data = seed_query_data()

    # Check to seed data only of it doesn't exist, otherwise it throws: ItegrityError for schedules 
    tables = ['destinations', 'pilots', 'flights', 'schedules']
    
    for table in tables:
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        if cursor.fetchone()[0] > 0:
            print("Data already seeded. Skipping...")
            return

    for insert_query in data: 
        cursor.execute(insert_query)

    conn.commit()
    print("data seeding complete..")

def init_db(): 
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    create_tables(cursor)
    seed_data(db_connection, cursor)

def fetch_query(query, params=None):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    if params:
        results = cursor.execute(query, params)
    else:
        results = cursor.execute(query)
        
    return results.fetchall()

def write_query(query, params):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    cursor.execute(query, params)
    db_connection.commit()







