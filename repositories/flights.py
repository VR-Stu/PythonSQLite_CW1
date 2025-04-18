from database import flight_management_db 

def fetch_all():
    # Parameterized query with %s, help to prevent from SQL injection
    query = """
        SELECT * FROM flights AS f
        JOIN destinations AS d1 ON f.OriginID = d1.DestinationID
        JOIN destinations AS d2 ON f.DestinationID = d2.DestinationID
    """    
    try:
        return flight_management_db.fetch_query(query)
    except Exception as e:
        print(f"Error in fetch_all: {e}")
        return [] # error, log and return empty result. 

def fetch_by_departure(date):
    # Parameterized query with %s, help to prevent from SQL injection
    query = """
        SELECT * FROM flights AS f
        JOIN destinations AS d1 ON f.OriginID = d1.DestinationID
        JOIN destinations AS d2 ON f.DestinationID = d2.DestinationID
        WHERE DATE(f.DepartureDate) = ? 
    """    
    try:
        return flight_management_db.fetch_query(query, (date,))
    except Exception as e:
        print(f"Error in fetch_by_departure: {e}")
        return [] # error, log and return empty result. 
    
def fetch_by_destination(destination):
    # Parameterized query with %s, help to prevent from SQL injection
    query = """
        SELECT * FROM flights AS f
        JOIN destinations AS d1 ON f.OriginID = d1.DestinationID
        JOIN destinations AS d2 ON f.DestinationID = d2.DestinationID
        WHERE d2.City = ? 
    """    
    try:
        return flight_management_db.fetch_query(query, (destination,))
    except Exception as e:
        print(f"Error in fetch_by_destination: {e}")
        return [] # error, log and return empty result. 
    
def fetch_by_status(status):
    # Parameterized query with %s, help to prevent from SQL injection
    query = """
        SELECT * FROM flights AS f
        JOIN destinations AS d1 ON f.OriginID = d1.DestinationID
        JOIN destinations AS d2 ON f.DestinationID = d2.DestinationID
        WHERE f.Status = ? 
    """    
    try:
        return flight_management_db.fetch_query(query, (status,))
    except Exception as e:
        print(f"Error in fetch_by_status: {e}")
        return []
    
def add_new_flight(flight_data):
    query = """
        INSERT INTO flights (FlightNumber, DepartureDate, DepartureTime, ArrivalTime, Status, OriginID, DestinationID)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    try:
        flight_management_db.write_query(query, flight_data)
        print("New flight added successfully.")

    except Exception as e:
        print(f"Error in add_new_flight: {e}")

def update_flight_info(flight_data):
    query = """
        UPDATE flights
        SET DepartureDate = ?, DepartureTime = ?, ArrivalTime = ?, Status = ?, OriginID = ?, DestinationID = ?
        WHERE FlightID = ?
    """
    try:
        flight_management_db.write_query(query, flight_data)
        print("Flight updated successfully.")

    except Exception as e:
        print(f"Error in update_flight_info: {e}")

def delete_flight_info(flight_id):
    query = "DELETE FROM flights WHERE FlightID = ?"
    try:
        flight_management_db.write_query(query, (flight_id,))
        print("Flight deleted successfully.")

    except Exception as e:
        print(f"Error in delete_flight_info: {e}")

