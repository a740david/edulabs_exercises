import concurrent.futures
import os
import threading
from datetime import datetime

import pytz
from concurrent.futures import ThreadPoolExecutor, wait
import requests

# 1
# def get_country(name:str):
#  list_name=name.split(",")
#  GENDERIZE_URL = "https://api.nationalize.io/"
#
#
#  for  name in list_name:
#
#   response1 = requests.get(GENDERIZE_URL ,params={"name": name})
#   list_country_id=response1.json()
#
#   list_probability=[]
#   for i in list_country_id['country'][::-1]:
#      list_probability.append(i['probability'])
#   max_=max(list_probability)
#
#   for i in list_country_id['country'][::-1]:
#    if max_ == i['probability']:
#        max_probability=i
#
#   country_id=max_probability['country_id']
#
#   COUNTRY_URL="https://restcountries.com/v3.1/alpha/"
#   response2=requests.get(COUNTRY_URL+country_id)
#   list_country=response2.json()
#
#   country = list_country[0]["name"]["common"]
#   continent = list_country[0]["region"]
#   languages = list_country[0]["languages"]
#   capital = list_country[0]["capital"][0]
#
#
#   IST = pytz.timezone(continent + '/' + capital)
#
#   if (response1.status_code or response2.status_code) < 400:
#      print(
#          f'country:{country},\n continent: {continent},\n languages: {languages},\n time in the country :{datetime.now(IST)}\n')
#   else:
#      raise Exception()
#
#  print(f"num nationality: {len(list_name)}")
#
#
#
# if __name__ == '__main__':
#     try:
#         #spain,philippines,philippines,spain,spain,spain,spain,spain,spain,spain
#         name = input("Insert 10 names: ")
#         start = datetime.utcnow()
#         get_country(name)
#         end = datetime.utcnow()
#         print(f"Time for all the names: {(end - start).total_seconds()}s")
#         #Time took: 13.789003s
#     except Exception:
#         print("Error ")


#2
# def list_names(name:str):
#     list_name = name.split(",")
#     executor=ThreadPoolExecutor(max_workers=10)
#     futures=[]
#     for name in list_name:
#         future=executor.submit(get_country,name)
#         futures.append(future)
#
#     done,not_done=wait(futures,return_when=concurrent.futures.ALL_COMPLETED)
#     print(f"done: {len(done)}")
#     print(f"not done: {len(not_done)}")
#
# def get_country(name:str):
#
#   GENDERIZE_URL = "https://api.nationalize.io/"
#
#   response1 = requests.get(GENDERIZE_URL ,params={"name": name})
#   list_country_id=response1.json()
#
#   list_probability=[]
#   for i in list_country_id['country'][::-1]:
#      list_probability.append(i['probability'])
#   max_=max(list_probability)
#
#   for i in list_country_id['country'][::-1]:
#    if max_ == i['probability']:
#        max_probability=i
#
#   country_id=max_probability['country_id']
#
#   COUNTRY_URL="https://restcountries.com/v3.1/alpha/"
#   response2=requests.get(COUNTRY_URL+country_id)
#   list_country=response2.json()
#
#   country = list_country[0]["name"]["common"]
#   continent = list_country[0]["region"]
#   languages = list_country[0]["languages"]
#   capital = list_country[0]["capital"][0]
#
#
#   IST = pytz.timezone(continent + '/' + capital)
#
#   if (response1.status_code or response2.status_code) < 400:
#      print(
#          f'country:{country},\n continent: {continent},\n languages: {languages},\n time in the country :{datetime.now(IST)}\n')
#   else:
#      raise Exception()
#
#
#
#
# if __name__ == '__main__':
#     try:
#         #spain,philippines,philippines,spain,spain,spain,spain,spain,spain,spain
#         name = input("Insert 10 names: ")
#         start = datetime.utcnow()
#         list_names(name)
#         end = datetime.utcnow()
#         print(f"Time took: {(end - start).total_seconds()}s")
#         #Time took: 1.57385s
#     except Exception:
#         print("Error ")

#3
