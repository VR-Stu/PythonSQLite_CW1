def seed_query_data():
    return [
    """INSERT INTO destinations (AirportName, AirportCode, City, Country) VALUES 
        ('Los Angeles International Airport', 'LAX', 'Los Angeles', 'USA'), 
        ('John F. Kennedy International Airport', 'JFK', 'New York', 'USA'),
        ('Heathrow Airport', 'LHR', 'London', 'UK'),
        ('Charles de Gaulle Airport', 'CDG', 'Paris', 'France'),
        ('Tokyo International Airport', 'HND', 'Tokyo', 'Japan'),
        ('Dubai International Airport', 'DXB', 'Dubai', 'UAE'),
        ('Sydney Kingsford Smith Airport', 'SYD', 'Sydney', 'Australia'),
        ('Berlin Brandenburg Airport', 'BER', 'Berlin', 'Germany'),
        ('Toronto Pearson International Airport', 'YYZ', 'Toronto', 'Canada'),
        ('Singapore Changi Airport', 'SIN', 'Singapore', 'Singapore')
    """,
    """INSERT INTO pilots (FirstName, LastName, DOB, LicenceNumber) VALUES 
        ('John', 'Doe', '1985-06-15', 'L123456'), 
        ('Jane', 'Smith', '1990-04-10', 'L654321'), 
        ('Mark', 'Johnson', '1982-09-25', 'L112233'), 
        ('Emily', 'Davis', '1995-01-18', 'L223344'),
        ('Michael', 'Brown', '1980-11-22', 'L556677'),
        ('Sarah', 'Wilson', '1992-03-14', 'L889900'),
        ('David', 'Moore', '1987-07-30', 'L334455'),(
        'Sophia', 'Taylor', '1994-08-09', 'L998877'),
        ('James', 'Anderson', '1988-12-05', 'L667788'),
        ('Olivia', 'Thomas', '1993-05-19', 'L223344')
    """,
    """INSERT INTO flights (FlightNumber, DepartureDate, DepartureTime, ArrivalTime, Status, OriginID, DestinationID) VALUES 
        ('AA101', '2025-04-20', '08:00', '10:30', 'Scheduled', 1, 2),
        ('BA202', '2025-04-20', '09:00', '11:30', 'Delayed', 2, 3),
        ('AF303', '2025-04-22', '12:00', '14:00', 'Scheduled', 3, 4),
        ('JL404', '2025-04-22', '14:00', '16:00', 'Scheduled', 4, 5),
        ('EK505', '2025-04-18', '16:30', '19:00', 'Departed', 5, 6),
        ('QF606', '2025-04-18', '17:00', '19:30', 'InFlight', 6, 7),
        ('LH707', '2025-04-18', '10:00', '12:30', 'InFlight', 7, 8),
        ('AC808', '2025-04-20', '11:00', '13:30', 'Scheduled', 8, 9),
        ('SQ909', '2025-04-15', '18:00', '20:30', 'Arrived', 9, 10),
        ('NZ010', '2025-04-15', '19:00', '21:30', 'Arrived', 10, 1);
    """,
    """INSERT INTO schedules (FlightID, PilotID, AssignedDate) VALUES 
        (1, 1, '2025-05-01'),
        (2, 2, '2025-05-01'),
        (3, 3, '2025-05-02'),
        (4, 4, '2025-05-02'),
        (5, 5, '2025-05-03'),
        (6, 6, '2025-05-03'),
        (7, 7, '2025-05-04'),
        (8, 8, '2025-05-04'),
        (9, 9, '2025-05-05'),
        (10, 10, '2025-05-05')
    """
    ]