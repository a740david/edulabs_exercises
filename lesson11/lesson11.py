import datetime

class NegetiveYear(Exception):
    pass

class YearFuturError(Exception):
    def __init__(self,msg):
        super().__init__(msg)


def get_age(birth_year:int) ->int:
    if birth_year<0:
        raise NegetiveYear()
    if birth_year>datetime.datetime.utcnow().year:
        raise NegetiveYear("Birth year not in range")
    return datetime.datetime.utcnow().year-birth_year

try:
    b_year=int(input("Insert your year: "))
    age=get_age(2050)
    print(f'You are{age} years old')
    print("Inside try after get_age")
except ValueError:
    print("you did not insert a number")
except NegetiveYear:
    print("negative year")
except Exception as e:
    print("e")
print("bye")

