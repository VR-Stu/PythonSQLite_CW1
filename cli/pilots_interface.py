from repositories import pilots 
from datetime import datetime

def get_valid_flight_assign_input():
    while True:
        user_input =  input("""
            Required (comma seperated): FlightID, PilotID, AssignedDate
            Example:  1,2,2025-04-18

            Enter:""")
        
        fields = user_input.split(",")
        print("fields", fields)
        try:
            # Validate
            flightID = int(fields[0])
            pilotID = int(fields[1])  

            assignedDate = fields[2]
            return (
                flightID,
                pilotID,
                assignedDate
            );   
        except ValueError:
            print("Invalid input try again.")

def format_result(pilots):
    print("-" * 70)
    print(f"{'ID':<5} {'First Name':<15} {'Last Name':<15} {'Date of Birth':<15} {'License No.':<15}")
    print("-" * 70)

    if not pilots:
        print("No records found.")

    for pilot in pilots:
        print(f"{pilot[0]:<5} {pilot[1]:<15} {pilot[2]:<15} {pilot[3]:<15} {pilot[4]:<15}")

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
                case 1:  # Back
                    return False
                case 2:  # Exit
                    return True
                case _:
                    print("Invalid option. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter a listed number.\n")

def format_schedules_result(schedules):
    print("-" * 180)
    print(f"{'First Name':<15} {'Last Name':<15} {'Licence Number':<15} {'Flight Number':<15} "
          f"{'Departure Date':<15} {'Departure Time':<15} {'Arrival Time':<15} {'Origin Airport':<25} "
          f"{'Destination Airport':<25}")
    print("-" * 180)

    if not schedules:
        print("No schedule information found.")

    for schedule in schedules:
        print(f"{schedule[0]:<15} {schedule[1]:<15} {schedule[2]:<15} {schedule[3]:<15} "
              f"{schedule[4]:<15} {schedule[5]:<15} {schedule[6]:<15} {schedule[7]:<25} "
              f"{schedule[8]:<25}")

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
                case 1:  # Back
                    return False
                case 2:  # Exit
                    return True
                case _:
                    print("Invalid option. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter a listed number.\n")

def handle_pilot_commands():
    while True:     
        user_input = input('''
            ====================================================
                    Pilots Menu - Manage Pilots Information
            ====================================================

            Please select one of the following options:

            1. View all Pilots
            2. View Pilot Schedule (by LicenceNumber)
            3. Assign Pilot to flights
                Required (comma seperated): FlightID, PilotID, AssignedDate

            4. Go Back to Main Menu
            5. Exit Application

            ----------------------------------------------------
            Select: ''')
        try:
            selected_option = int(user_input)
            match selected_option:
                case 1: # View all Pilots
                    db_result = pilots.fetch_all()

                    # format data for view
                    result = format_result(db_result)
                    if result:
                        return True
                case 2: # View Pilot Schedule (by Licence Number)
                    user_licence = input("Enter Licence Number: (e.g L123456): ")

                    db_result = pilots.fetch_schedules_by_licenceNumber(user_licence)

                    # format data for view
                    result = format_schedules_result(db_result)
                    if result:
                        return True                    
                case 3: #Assign Pilot to flights
                    assign_input = get_valid_flight_assign_input();
                    pilots.assign_flight(assign_input)
                case 4: 
                    return False # Return without exit (hence false)
                case 5:
                    return True # Return with exit (hence true)
                case _:
                    print("Invalid pilot menu option. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter a listed number.\n")
