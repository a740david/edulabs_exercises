from lesson9.rav_kav.rides import Rides
from lesson9.rav_kav.rav_kav import RavKav
import datetime
if __name__=='__main__':
    rav_kav=RavKav(208937494,'ziv')
    topup=rav_kav.topup(35)
    get_current_balance= rav_kav.get_current_balance()

    rides=Rides()
    rides.ride(datetime.datetime(2023, 12, 10).date(),40,rav_kav)
    rides.ride(datetime.datetime(2023, 12, 10).date(), 4, rav_kav)
    rides.ride(datetime.datetime(2023, 12, 10).date(), 3, rav_kav)
    get_current_balance = rav_kav.get_current_balance()

    get_rides_by_date=rides.get_rides_by_date(datetime.datetime(2023, 12, 10).date())
    get_rides_by_type=rides.get_rides_by_type("short")
    print(get_current_balance)
    print(get_rides_by_date)
    print(get_rides_by_type)