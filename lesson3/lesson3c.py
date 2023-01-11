
#1
import copy

goods = [['apple', 'pear', 'peach', 'chery' ],
['salak', 'mangustin', 'mango', 'durian', 'breadfruit',
    'bayberry', 'blueberry', 'cloudberry' , 'raspberry', 'blackberry' ]]

#a
# goods1=[]
# for i in goods:
#     if type(i)==str:
#         goods1.append(i)
#     elif type(i)==list:
#         for j in i:
#             goods1.append(j)
#
# max_of_word=len(max(goods1,key=len))
#
# index=0
# for i in goods:
#     if(type(i)==str):
#         if len(i)==max_of_word:
#             print(index)
#             index=index+1
#     elif (type(i)==list):
#          indexlist=0
#          for j in i:
#              if len(j)==max_of_word:
#                  print(str(index)+","+str(indexlist))
#              indexlist=indexlist+1
#          index = index + 1
#
#
# #b
# goods1=[]
# for i in goods:
#     if type(i)==str:
#         goods1.append(i)
#     elif type(i)==list:
#         for j in i:
#             goods1.append(j)
#
# max_of_word=len(max(goods1,key=len))
# string_of_words=[]
# for i in goods1:
#     if len(i)==max_of_word:
#         string_of_words.append(i)
# print(string_of_words)
# sum_of_words= "".join(string_of_words)
# counter=0
# for i in sum_of_words:
#     if i=="a" or i=="i" or i=="e" or i=="o" or i=="u":
#         counter+=1
# print(counter)

#2
# index=0
# for i in goods:
#     if (type(i)==list):
#          indexlist=0
#          for j in i:
#              if j[0]=="a" or j[0]=="e" or j[0]=="i" or j[0]=="o" or j[0]=="u":
#                  print(str(index)+","+str(indexlist))
#              indexlist=indexlist+1
#          index = index + 1


# 3
# index=0
# new_list=[]
# for i in goods:
#     if (type(i)==list):
#          indexlist=0
#          for j in i:
#              if j.find("b") != -1:
#                  new_list.append(j)
#              indexlist=indexlist+1
#          index = index + 1
# print(new_list)

#5
# goods1=[]
# for i in goods:
#     if type(i)==str:
#         goods1.append(i)
#     elif type(i)==list:
#         for j in i:
#             goods1.append(j)
#
# max_of_word=len(min(goods1,key=len))
#
# index=0
# for i in goods:
#     if(type(i)==str):
#         if len(i)==max_of_word:
#             print(index)
#             index=index+1
#     elif (type(i)==list):
#          indexlist=0
#          for j in i:
#              if len(j)==max_of_word:
#                  print(str(index)+","+str(indexlist))
#              indexlist=indexlist+1
#          index = index + 1

#6
# index=0
# for i in goods:
#     if (type(i)==list):
#          indexlist=0
#          for j in i:
#              if j.find("berry") != -1:
#                  print(str(index) + "," + str(indexlist))
#              indexlist=indexlist+1
#          index = index + 1

#7

# for i in goods:
#     if (type(i)==list):
#          indexlist=0
#          for j in i:
#              if indexlist%2!=0 :
#                  print(j+str(2))
#              indexlist =indexlist+1

#8
# goods1=[]
# for i in goods:
#     if (type(i)==list):
#         for j in i:
#             if j.find("p")!=-1:
#                 goods1.append(j[::-1])
# print(goods1)

#9
# goods1=[]
# for i in goods:
#     if (type(i)==list):
#         for j in i:
#             if len(j)>5:
#                 print(j)
#
# 11
# lo=[]
# for i in goods:
#     if type(i)==list:
#         lo.append(copy.copy(i))
# index=0
#
# for i in lo:
#     if (type(i)==list):
#          indexlist=0
#          for j in i:
#             lo[index][indexlist]=j[0:3]
#             indexlist=indexlist+1
#     index=index+1
# print(lo)
# print(goods)

