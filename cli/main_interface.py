from cli import destinations_interface
from cli import flights_interface
from cli import pilots_interface
from repositories import destinations

def start():
    exit_app = False
    defaultMessage = '''
        ====================================================
            Welcome to the Flight Management Application!
        ====================================================

        Please select one of the following options:

        1.  Flights Information
                └─── View | Update | Create

        2.  Destinations Information
                └─── View | Update

        3.  Pilots Information
                └─── View | Update (assign flights)

        4.  Get Number of Flights to each destination

        5.  Exit the application
    '''

    while not exit_app:        
        print(defaultMessage)
        user_input = input("Select: ")

        try: 
            selected_option = int(user_input)

            match selected_option:
                case 1: # Flights Information
                    result = flights_interface.handle_flight_commands()
                    if result:
                        exit_app = True

                case 2: # Destinations Information
                    result = destinations_interface.handle_destinations_commands() 
                    if result:
                        exit_app = True

                case 3: # Pilots Information
                    result = pilots_interface.handle_pilot_commands() 
                    if result:
                        exit_app = True

                case 4: # Get Number of Flights to Destination
                    db_result = destinations.count_destination_flights()
                    print(db_result)
                case 5:
                    exit_app = True

                case _:
                    print("Looks like that operation is not recognized, please try again...")
        except:
            print('Sorry, your option is invalid, try again!')
