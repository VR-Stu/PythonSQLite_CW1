from repositories import destinations

def get_updated_destination_input():
    while True:        
        user_input =  input("""
            Required (comma seperated): AirportName, AirportCode, City, Country, DestinationID
            Example: Heathrow Airport,LHR,London,UK,2

            Enter:""")

        # get all fields 
        fields = user_input.split(",")

        if len(fields) != 5:
            print("Invalid input. Please enter exactly 5 required fields.")
    
        return (
            fields[0], # AirportName
            fields[1], # AirportCode
            fields[2], # City
            fields[3], # Country
            fields[4], # DestinationID
        )

def get_valid_country_input():
    while True:
        user_input = input("Enter country name (only letters allowed): ")
        
        # Validate if the input contains only alphabetic characters
        if user_input.isalpha():
            return user_input
        else:
            print("Only alphabetical characters are allowed. Please try again.")

def format_result(destinations):
    print("-" * 105)
    print(f"{'DestinationID':<14} {'AirpotName':<50} {'AirpotCode':<14} {'City':<14} {'Country':<14}")
    print("-" * 105)

    if not destinations:
        print("No destinations found.")

    for destination in destinations:
        print(f"{destination[0]:<14} {destination[1]:<50} {destination[2]:<14} {destination[3]:<14} {destination[4]:<14}")

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

def handle_destinations_commands():
    while True:
        print('''
            ====================================================
             Destinations Menu - Manage Destination Information
            ====================================================

            Please select one of the following options:

            1. View All Destinations
            2. View Destination By Country (USA, UK)
            3. Update Destination
                Required (comma seperated): AirportName, AirportCode, City, Country, DestinationID
              
            4. Go Back to Main Menu
            5. Exit Application

            ----------------------------------------------------
            ''')
        
        user_input = input("Select: ")
        try:
            selected_option = int(user_input)
            match selected_option:
                case 1: # View All Destinations
                    db_result = destinations.fetch_all()

                    # format data for view
                    result = format_result(db_result)
                    if result:
                        return True                    
                case 2: # View Destination By Country
                    user_input = get_valid_country_input()
                    db_result = destinations.fetch_by_country(user_input)

                    # format data for view
                    result = format_result(db_result)
                    if result:
                        return True
                case 3: # Update Destination
                    updated_destination = get_updated_destination_input()

                    # write to db
                    destinations.update_destination(updated_destination)
                case 4:
                    return False # Return without exit (hence false)
                case 5:
                    return True # Return with exit (hence true)
                case _:
                    print("Invalid destination menu option. Try again.\n")
        except ValueError:
            print("Invalid input. Please enter a listed number.\n")