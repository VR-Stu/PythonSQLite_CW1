from database import flight_management_db
from cli import main_interface

print('Application starting...') 

# seed database before use
flight_management_db.init_db()

# start cli interface
main_interface.start()