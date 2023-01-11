import pprint
#1
# def func(original_dict):
#     list=[None,[],""]
#     new_dict={}
#     for key,value in original_dict.items():
#       if(value  not in list):
#           new_dict[key]=value
#     print(new_dict)
#
#
# original_dict={'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': ""}
# print((func(original_dict)))

#2
# def func(orginal_list):
#  dictionary_list={}
#  for i in orginal_list:
#       if type(i)==tuple:
#             if i[0]  in dictionary_list:
#               dictionary_list[i[0]].append(i[1])
#             else:
#                dictionary_list[i[0]]=[i[1]]
#  return dictionary_list
#
#
# original_list=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# print((func(original_list)))

#3



# def func(dictionary_of_lists):
#  dict_={}
#
#  list_of_dictionary=[]
#  counter=0
#  j=0
#  for k,v in dictionary_of_lists.items():
#      if j==0:
#         for i in v:
#             list_of_dictionary.append({k:i})
#
#         j=1
#      else:
#
#        for i in v:
#            list_of_dictionary[counter][k]=i
#            counter=counter+1
#  print(list_of_dictionary)
#
# dictionary_of_lists={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# (func(dictionary_of_lists))

