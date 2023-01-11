
#1
# def func(list_name):
#   words=list_name.split("-")
#   words.sort()
#   arr_name="-".join(words)
#   return arr_name
# list_name="green-red-yellow-black-white"
# print(func(list_name))

2
#
# def insert_():
#  words = [item for item in input("Enter the list items : ").split()]
#  return words
#
# def search(words):
#     arr_names=[]
#     digit=input("enter the digit: ")
#     number=int(insert_("enter the number: "))
#     for i in words:
#         if(type(i)==str):
#             for j in i:
#               if j==digit:
#                 arr_names.append(i)
#         if arr_names.count(i)>1:
#             arr_names.remove(i)
#     return arr_names
# print(search(insert_()))

#3
# def sum(string_sentence):
#  counter_upper=(0)
#  counter_lower=(0)
#  for i in string_sentence:
#     if i.isupper() :
#          counter_upper+=1
#     if i.islower():
#          counter_lower+=1
#  sum_= str(counter_lower)+str(counter_upper)
#  sum_tuple=tuple(sum_)
#  return sum_tuple
#
# string_sentence=input("enter the string: ")
# print(sum(string_sentence))