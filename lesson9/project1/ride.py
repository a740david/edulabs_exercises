import random
class Ride:
    def __init__(self,origin_time,destination_time,driver_name):
        self.id=random.randint(0,10)
        self.origin_time=origin_time
        self.destination_time=destination_time
        self.driver_name=driver_name
        self.delays=0

    def __str__(self):
        return f'scheduled_ride: \n {self.origin_time} \n {self.destination_time} \n {self.driver_name}'

