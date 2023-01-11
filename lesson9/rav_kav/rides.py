from datetime import datetime
from lesson9.rav_kav import rav_kav


now= datetime.now()
date = now.strftime("%d/%m/%Y")

class Rides(rav_kav.RavKav):
    def __init__(self):
        self.rides_log={}
        self.rides_type={"short":0,"medium":0,"long":0}
        #{ride type:[2022-12-12 16:26:16.987332]}

    def ride(self,date,amount_of_km, ravKav):

        if amount_of_km<0:
            return f'ERROR There is not enough money for the trip{amount_of_km}'
        if date in self.rides_log.keys():
            self.rides_log[date] = self.rides_log[date] + 1
        else:
            self.rides_log[date] =1
        if amount_of_km<=15:
            self.rides_type["short"]=self.rides_type["short"]+1
            ravKav.balance=ravKav.balance-5.5
        elif amount_of_km<=40:
            self.rides_type["medium"] = self.rides_type["medium"] + 1
            ravKav.balance = ravKav.balance - 12
        elif amount_of_km>40:
            self.rides_type["long"] = self.rides_type["long"] + 1
            ravKav.balance = ravKav.balance - 23


    def get_rides_by_date(self,date):
        counter=self.rides_log[date]
        return f'returns travel amount: {counter}'

    def get_rides_by_type(self,ride_type):
       counter=self.rides_type[ride_type]
       return f'return amount of  rides of this type: {counter}'