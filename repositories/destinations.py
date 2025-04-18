from database import flight_management_db 

def fetch_all():
    query = """SELECT * FROM destinations"""    
    try:
        return flight_management_db.fetch_query(query)
    except Exception as e:
        print(f"Error in fetch_by_departure: {e}")
        return [] 

def fetch_by_country(country):
    # Parameterized query with %s, help to prevent from SQL injection
    query = """
        SELECT * FROM destinations WHERE Country = ? 
    """    
    try:
        return flight_management_db.fetch_query(query, (country,))
    except Exception as e:
        print(f"Error in fetch_by_departure: {e}")
        return []

def update_destination(data):
    query = """
        UPDATE destinations
        SET AirportName = ?, AirportCode = ?, City = ?, Country = ?
        WHERE DestinationID = ?
    """
    try:
        flight_management_db.write_query(query, data)
        print("Destination updated successfully.")

    except Exception as e:
        print(f"Error in update_flight: {e}")

def count_destination_flights():
    query = """
            SELECT 
                d.Country,
                COUNT(f.FlightID) AS NumberOfFlights
            FROM 
                flights f
            JOIN 
                destinations d ON f.DestinationID = d.DestinationID
            GROUP BY 
                d.Country
        """
    try:
        flight_management_db.fetch_query(query)
    except Exception as e:
        print(f"Error in count_destination_flights: {e}")