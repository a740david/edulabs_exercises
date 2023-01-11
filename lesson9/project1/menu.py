import pickle

from lesson9.project1.best_bus_company import BestBusCompany
import datetime
import os
#
# from datetime import datetime


class Menu():



        flag = False
        print('------menu------')
        select = input('select Manager or Passenger: ')
        if select == "Passenger":
            print (f'Connected \n')
        elif select == "Manager":
            i = 0
            while (not flag and i < 3):
                password = input('entert the password: ')
                if password == 'RideWithUs!':
                    flag = True
                i = i + 1
            if flag:
                print('conected')
                x=BestBusCompany()

                select1=input('Select add or delete or update: ')

                match select1:
                    case 'add':
                        x.add_bous_route(56, "tel-aviv", "Haifa", ["hadera" ,"netanya"])
                        x.add_bous_route(5, "tel-aviv", "Haifa", ["hadera" ,"netanya"])
                        for i in x.list_of_bus_route:
                            print (i)
                    case 'delete':
                        sure_to_delete=input('Are you sure?: ')
                        if sure_to_delete=='yes':
                            x.add_bous_route(56, "tel-aviv", "Haifa", ["hadera" ,"netanya"])
                            x.add_bous_route(5, "tel-aviv", "Haifa", ["hadera" ,"netanya"])
                            x.delete_bous_route(5)
                            for i in x.list_of_bus_route:
                                print(i)
                            print('The bus route has been deleted')
                        elif(sure_to_delete=='no'):
                            print('returns to the menu')
                        else:
                            print('Error Nothing selected')
                    case 'update':
                        x.add_bous_route(5, "tel-aviv", "Haifa",["hadera" ,"netanya"])
                        x.update_bous_route(5)
                        select2=input('Select origin or destination or list_of_stops: ')
                        match select2:
                            case 'origin':
                                new_origin=input('new_origin: ')
                                x.update_origin_(5,new_origin)
                                x.update_bous_route(5)
                            case 'destination':
                                new_destination = input('new_destination: ')
                                x.update_destination_(5, new_destination)
                                x.update_bous_route(5)
                            case 'list_of_stops':
                                select3=input('Select add_station or remove_station: ')
                                match select3:
                                    case 'add_station':
                                        new_station=input('adding_a_station_to_the_list: ')
                                        x.add_a_station_(5, new_station)
                                        x.update_bous_route(5)
                                    case 'remove_station':
                                        remove_station=input('remove_a_station_to_the_list: ')
                                        x.remove_a_station_(5,remove_station)
                                        x.update_bous_route(5)
                                    case 'Station update':
                                        station = input('remove_station: ')
                                        update_station=input('Update a station in the list: ')
                                        x.update_station_(5, station ,update_station )
                                        x.update_bous_route(5)
                    case 'add_scheduled_ride':

                        x.add_bous_route(5, "tel-aviv", "Haifa", ["hadera", "netanya"])
                        x.add_scheduled_ride(5, datetime.time(10, 30, 18), datetime.time(12, 20,10), 'oz')
                        x.add_scheduled_ride(5,datetime.time(3, 12, 24) ,datetime.time(5, 30, 28) , 'ziv')
                        x.show_scheduled_ride(5)
                        flag=True
                        while flag:
                         new_ride=input('Want to add a new ride?: ')
                         if new_ride=='yes':
                           origin_time=input("enter the time: ")
                           destinotion_time=input("enter the time: ")
                           driver_name=input('enter driver_name: ')
                           x.add_scheduled_ride(5,origin_time,destinotion_time,driver_name)
                           x.show_scheduled_ride(5)
                           flag=True




            else:
                print (f'Erorr Due to several failed attempts, login failed')
        else:
             print(f'erorr')


# if __name__=='__main__':

if __name__ == '__main__':

    # check whether this is the first time you run the app
    # if this is the first time - create a new class
    if not os.path.exists('menu.pickle'):
        menu = Menu()
        # menu.select()
    else:
        # this is not the first time - we already have a DB
        # with data from the previous runs
        with open('menu.pickle', 'rb') as fh:
            menu = pickle.load(fh)


