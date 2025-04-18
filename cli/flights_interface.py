from repositories import flights
from datetime import datetime

allowed_statuses = ["Scheduled", "Delayed", "Departed", "InFlight", "Arrived"]

def get_valid_date_input():
    while True:
        user_input = input("Enter departure date (YYYY-MM-DD): ")
        try:
            # Validate date format
            datetime.strptime(user_input, "%Y-%m-%d")
            return  user_input;   
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

def get_valid_flightID_input():
    while True:
        user_input = input("Enter FlightID: ")
        try:
            # Validate number input
            return int(user_input)  
        except ValueError:
            print("Invalid input, FlightID should be a number")

def get_valid_status_input():
    while True:
        
        user_input = input("Enter status (Scheduled, Delayed, Departed, InFlight, or Arrived): ")
        
        # Ensure status value is allowed.
        if user_input in allowed_statuses:
            return user_input
        else: 
            print("Invalid status. Please enter one of the following:")
            print(", ".join(allowed_statuses))

def get_new_flight_data_input():
    while True:        
        user_input =  input("""
            Required (comma seperated): FlightNumber, DepartureDate, DepartureTime, ArrivalTime, Status, OriginID, DestinationID
            Example:  BB123,2025-03-01,08:00,12:00,Scheduled,1,2

            Enter:""")

        # get all fields 
        fields = user_input.split(",")

        if len(fields) != 7:
            print("Invalid input. Please enter exactly 7 required fields.")
        
        if fields[4] not in allowed_statuses:
            print("Invalid status. Please enter one of the following:")
            print(", ".join(allowed_statuses))
            
        try:
            origin_id = int(fields[5])
            destination_id = int(fields[6])            
        except ValueError:
            print("OriginID and DestinationID must be integers.")
            continue
    
        return (
            fields[0], # FlightNumber
            fields[1], # DepartureDate
            fields[2], # DepartureTime
            fields[3], # ArrivalTime
            fields[4], # Status
            origin_id,
            destination_id
        )

def get_updated_flight_data_input():
    while True:        
        user_input =  input("""
            Required (comma seperated): DepartureDate, DepartureTime, ArrivalTime, Status, OriginID, DestinationID, FlightID
            Example:  2025-03-01,08:00,12:00,Scheduled,1,2,1

            Enter:""")

        # get all fields 
        fields = user_input.split(",")

        if len(fields) != 7:
            print("Invalid input. Please enter exactly 7 required fields.")
        
        if fields[3] not in allowed_statuses:
            print("Invalid status. Please enter one of the following:")
            print(", ".join(allowed_statuses))
            
        try:
            origin_id = int(fields[4])
            destination_id = int(fields[5])            
        except ValueError:
            print("OriginID and DestinationID must be integers.")
            continue
    
        return (
            fields[0], # DepartureDate
            fields[1], # DepartureTime
            fields[2], # ArrivalTime
            fields[3], # Status
            origin_id,
            destination_id,
            fields[6], # FlightID
        )

def format_result(flights):
    print("-" * 115)
    print(f"{'Flight ID':<10}  {'Flight Number':<14} {'Date':<12} {'From City':<16} {'To City':<16} {'Departure Time':<15} {'Arrival Time':<15} {'Status':<15}")
    print("-" * 115)

    if not flights:
        print("No flights found.")

    for flight in flights:
        print(f"{flight[0]:<10} {flight[1]:<14} {flight[2]:<12} {flight[11]:<16} {flight[16]:<16} {flight[3]:<15} {flight[4]:<15} {flight[5]:<15}")

    while True:
        user_input = input('''
            Please select one of the following options:

            1. Go Back to Previous Menu
            2. Exit Application
            ----------------------------------------------------
        ''')
        try:
            selected_option = int(user_input)
            match selected_option:
                case 1: # Back
                    return False
                case 2:
                    return True
                case _:
                    print("Invalid option. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter a listed number.\n")

def handle_flight_commands():
    while True:
        user_input = input('''
            ====================================================
                Flights Menu - Manage Flight Information
            ====================================================

            Please select one of the following options:
            
            0. View all
            1. View by Departure Date (YYYY-MM-DD)
            2. View by Destination (City name: e.g London)
            3. View by Status (Scheduled, Delayed, Departed, InFlight, Arrived)
            4. Add New Flight:
                Required: (FlightNumber, DepartureDate, DepartureTime, ArrivalTime, Status, OriginID, DestinationID)
                                               
            5. Update Flight Information
                Required: (FlightNumber, DepartureDate, DepartureTime, ArrivalTime, Status, OriginID, DestinationID)
            
            6. Delete Flight Information
                Required: (FlightID)
                           
            7. Go Back to Main Menu
            8. Exit Application

            ----------------------------------------------------
        ''')
        try:
            selected_option = int(user_input)
            match selected_option:
                case 0:
                    # fetch from db
                    db_result = flights.fetch_all()

                    # format data for view
                    result = format_result(db_result)
                    if result:
                        return True 
                case 1: # View by Departure Date

                    # Validate input 
                    user_date = get_valid_date_input()

                    # fetch from db
                    db_result = flights.fetch_by_departure(user_date)

                    # format data for view
                    result = format_result(db_result)
                    if result:
                        return True                        
                case 2: # View by Destination (City name: e.g London)

                    # no validtion needed, simply return empty resut
                    user_date = input("Enter destination: ")

                    # fetch from db
                    db_result = flights.fetch_by_destination(user_date)

                    # format data for view
                    result = format_result(db_result)
                    if result:
                        return True   
                case 3: # View by Status
                    user_status = get_valid_status_input()
                    
                    # fetch from db
                    db_result = flights.fetch_by_status(user_status)

                    # format data for view
                    result = format_result(db_result)
                    if result:
                        return True 
                case 4: # Add New Flight
                    new_flight = get_new_flight_data_input()

                    # write to db
                    flights.add_new_flight(new_flight)
                case 5: # Update Flight Information
                    # get user input
                    updated_flight = get_updated_flight_data_input()

                    # write to db
                    flights.update_flight_info(updated_flight)
                case 6: # Delete Flight Information
                    flight_id = get_valid_flightID_input()
                    flights.delete_flight_info(flight_id)
                case 7:
                    return False # Return without exit (hence false)
                case 8:
                    return True # Return with exit (hence true)
                case _:
                    print("Invalid flight menu option. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter a listed number.\n")
        