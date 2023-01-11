import csv
import os

# if __name__ == "__main__":
#
#     def files():
#
#         counter = 0
#         with open("AAPL.csv", "r") as fh:
#             for line in fh:
#                 counter+=1
#         sum_rows=counter
#         return sum_rows
#
#
#     print (files())

# initializing data to be stored in db
import pickle
student = {
    'name': 'David',
    'city': 'Tel Aviv',
    'grades': {'math':[98, 87, 90],
               'english': [85]
               }
}
with open('test.pckl', 'wb') as fh:
    pickle.dump(student, fh)


with open('test.pckl', 'rb') as fh:
    my_data = pickle.load(fh)

print(my_data)