from lesson9.project1.ride import Ride

class BusRoute:

    def __init__(self,line_number:int,origin:str,destination,list_of_stops):
     self.line_number=line_number
     self.origin=origin
     self.destination=destination
     self.list_of_stops=list_of_stops
     self.scheduled_rides=[]

    # def get_type(self):
    #     return type(self.list_of_stops)
    #
    def getlinenumber(self):
        return self.line_number

    # def get_scheduled_rides(self):
    #     for i in self.scheduled_rides:
    #         return i

    def delete_route(self):
            self.line_number=None
            self.origin=None
            self.destination=None
            self.list_of_stops=None

    def update_origin(self,origin):
            self.origin=origin

    def update_destination(self,destination):
            self.destination=destination

    def add_a_station(self,adding_a_station_to_the_list):
            self.list_of_stops.append(adding_a_station_to_the_list)

    def remove_a_station(self,remove_a_station_to_the_list):
            self.list_of_stops.remove(remove_a_station_to_the_list)

    def update_station(self, station ,update_a_station_in_the_list):
            for i in range(len(self.list_of_stops)):
                if self.list_of_stops[i]==station:
                   self.list_of_stops[i]=update_a_station_in_the_list

    def add_ride_in_scheduled_ride(self ,origin_time,destination_time,driver_nam):
        x=Ride(origin_time,destination_time,driver_nam)
        self.scheduled_rides.append(x)

    def add_scheduled_ride(self ,line_number):
            for i in self.scheduled_rides:
                if line_number==self.line_number:
                     print(i)

    def __str__(self):
     return f'BusRoute is: \n number line: {self.line_number} ' \
            f',\n origin: {self.origin},\n destination: {self.destination},\n list_of_stops: {self.list_of_stops} '





