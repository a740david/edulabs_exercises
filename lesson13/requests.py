from datetime import datetime

import pytz

import requests


def get_ethnicit():
 GENDERIZE_URL = "https://api.nationalize.io/"
 name = input("Insert your name: ")
 response1 = requests.get(GENDERIZE_URL ,params={"name": name})
 list_country_id=response1.json()

 list_probability=[]
 for i in list_country_id['country'][::-1]:
     list_probability.append(i['probability'])
 max_=max(list_probability)

 for i in list_country_id['country'][::-1]:
   if max_ == i['probability']:
       max_probability=i

 country_id=max_probability['country_id']

 COUNTRY_URL="https://restcountries.com/v3.1/alpha/"
 response2=requests.get(COUNTRY_URL+country_id)
 list_country=response2.json()

 country = list_country[0]["name"]["common"]
 continent = list_country[0]["region"]
 languages = list_country[0]["languages"]
 capital = list_country[0]["capital"][0]


 IST = pytz.timezone(continent + '/' + capital)

 if (response1.status_code or response2.status_code) < 400:
     print(
         f'country:{country},\n continent: {continent},\n languages: {languages},\n time in the country :{datetime.now(IST)}')
 else:
     raise Exception()



if __name__ == '__main__':
    try:
        get_ethnicit()
    except Exception:
        print("Error ")