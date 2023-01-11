class Apartment:
  def __init__(self ,country:str,city:str,street:str,house_number:int,flat_number:int,
               rooms_number:int,size_of_room:list,size_of_balcomies:list,amount_of_bathrooms:int
               ,size_of_bathrooms:list,kitchen_size:float,total_flats_size:float):
       self.country=country
       self.city=city
       self.street=street
       self.house_number=house_number
       self.flat_number=flat_number
       self.rooms_number=rooms_number
       self.size_of_room=size_of_room
       self.balconies=True
       self.size_of_balcomies=size_of_balcomies
       self.amount_of_bathrooms=amount_of_bathrooms
       self.size_of_bathrooms=size_of_bathrooms
       self.kitchen_size=kitchen_size
       self.total_flats_size=total_flats_size
       print(f"country: {country} | city:{city} | street:{street} | house_number: {house_number} | flat_number:{flat_number}")

  def get_rooms_number(self):
      if(self.rooms_number<0):
          print("erorr")
      else:
       return self.rooms_number

  def get_living_space_size(self):
      if self.rooms_number!=len(self.size_of_room):
          print("The number of rooms cannot be different from a number of the size of the array that contains the room")
      else:
          sum_of_size_rooms=sum(self.size_of_room)
          return sum_of_size_rooms

  def get_area_of_balconies(self):
      if self.balconies==False:
          print("There are no balconies")
      else:
          sum_of_size_balconies=sum(self.size_of_balcomies)
          return sum_of_size_balconies

  def get_annual_rent(self,property_tax_rate):
      print("---------------")
      monthly_property_tax=(property_tax_rate*self.total_flats_size)+(property_tax_rate*0.75*self.get_area_of_balconies())
      return print(f"monthly_property_tax: {monthly_property_tax}")
apartment=Apartment('israel','tel-aviv','igal-alon',house_number=7,flat_number=2,rooms_number=4,size_of_room=[9,5,3,5.5]
                   , size_of_balcomies=[10,11.5],amount_of_bathrooms=2,size_of_bathrooms=[5,4],kitchen_size=22,total_flats_size=105)

apartment.get_rooms_number()
apartment.get_living_space_size()
apartment.get_area_of_balconies()
apartment.get_annual_rent(2)
