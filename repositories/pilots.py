from database import flight_management_db 

def fetch_all():
    query = """SELECT * FROM pilots"""    
    try:
        return flight_management_db.fetch_query(query)
    except Exception as e:
        print(f"Error in fetch_all: {e}")
        return [] 
    
def fetch_schedules_by_licenceNumber(licenceNumber):
    # Parameterized query with placeholders to prevent SQL injection
    query = """
        SELECT 
            p.FirstName,
            p.LastName,
            p.LicenceNumber,
            f.FlightNumber,
            f.DepartureDate,
            f.DepartureTime,
            f.ArrivalTime,
            d1.AirportName,
            d2.AirportName
        FROM schedules AS s
        JOIN pilots AS p ON s.PilotID = p.PilotID
        JOIN flights AS f ON s.FlightID = f.FlightID
        JOIN destinations AS d1 ON f.OriginID = d1.DestinationID
        JOIN destinations AS d2 ON f.DestinationID = d2.DestinationID 
        WHERE p.LicenceNumber = ?
    """    
    try:
        return flight_management_db.fetch_query(query, (licenceNumber,))
    except Exception as e:
        print(f"Error in fetch_by_name: {e}")
        return []

def assign_flight(data):
    print("wtf", data)
    query = """
        INSERT INTO schedules (FlightID, PilotID, AssignedDate)
        VALUES (?, ?, ?)
    """
    try:
        flight_management_db.write_query(query, data)
        print("New flight assigned successfully.")
    except Exception as e:
        print(f"Error in assign_flight: {e}")