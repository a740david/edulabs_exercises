from lesson9.project1.bus_route import BusRoute


class BestBusCompany:



      def __init__(self):
         self.list_of_bus_route=[]




      def add_bous_route(self,line_number,origin,destination,list_of_stops):
          x=BusRoute(line_number,origin,destination,list_of_stops)
          self.list_of_bus_route.append(x)

      def delete_bous_route(self,line_number):
          for i in self.list_of_bus_route:
              if i.getlinenumber()==line_number:
                  i.delete_route()
                  self.list_of_bus_route.remove(i)

      def search_line(self,line_number):
          for i in self.list_of_bus_route:
              if i.getlinenumber() == line_number:
                  return  i
      def update_bous_route(self,line_number):
          print(self.search_line(line_number))

      def update_origin_(self,line_number,origin):
          x=self.search_line(line_number)
          x.update_origin(origin)

      def update_destination_(self,line_number,destination):
          x = self.search_line(line_number)
          x.update_destination(destination)

      def add_a_station_(self,line_number,adding_a_station_to_the_list):
          x = self.search_line(line_number)
          x.add_a_station(adding_a_station_to_the_list)

      def remove_a_station_(self,line_number,remove_a_station_to_the_list):
          x = self.search_line(line_number)
          x.remove_a_station(remove_a_station_to_the_list)

      def update_station_(self,line_number,station,update_a_station_in_the_list):
          x = self.search_line(line_number)
          x.update_station(station,update_a_station_in_the_list)

      def add_scheduled_ride(self,line_number,origin_time,destination_time,driver_nam):
          x= self.search_line(line_number)
          x.add_ride_in_scheduled_ride(origin_time,destination_time,driver_nam)

      def show_scheduled_ride(self,line_number):
          x= self.search_line(line_number)
          x.add_scheduled_ride(line_number)

