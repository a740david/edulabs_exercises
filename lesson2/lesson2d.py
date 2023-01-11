#1
# i=0
# while i<10:
#     i=i+1
#     print(i)

#2
# number=int(input("enter: "))
# i=0
# while i<number-3:
#     i=i+3
#     print(i)

#3
# end_of_input = False
# sum=0
# counter=0
# while not end_of_input:
#  numbers = input("enter the numbers: ")
#  if(numbers=='/'):
#      end_of_input=True
#  else:
#      sum +=int(numbers)
#      counter+=1
# average=sum/counter
# print(sum)
# print(average)

#4


# end_of_input = False
# list_names=""
# numbers_students=0
# counter=0
# while not end_of_input:
#     names = input("enter names: " )
#     grades = input("enter the grades: ")
#     if(names =='$$$' or grades=='$$$'):
#         end_of_input=True
#     else:
#         list_names+=names
#         numbers_students+=1
#         counter+=1
#         average =  int(grades)/ counter
# print(list_names)
# print(numbers_students)
# print(average)

#5
# end_of_input = False
# sum_digits=0
# counter=0
# sum_characters=0
# while not end_of_input:
#   string_user=input("enter the string: ")
#   if(string_user=='$'):
#       end_of_input=True
#   else:
#       counter+=1
#       sum_characters += string_user.count("") - 1
#       if(string_user.isdigit()):
#           sum_digits+=string_user.count("")-1
#
# print(counter)
# print(sum_characters)
# print(sum_digits)



#6
# end_of_input = False
# counter=0
# sum_length=0
# i=0
# arr_of_len=[]
# while not end_of_input:
#
#     if(counter==5):
#         end_of_input=True
#     else:
#         strings = input('enter ten strings: ')
#         arr_of_len.append(strings.count('')-1)
#     counter += 1
#
#
# arr_of_len.sort()
#
#
# counter1=1
# while i<len(arr_of_len)-1:
#     if(arr_of_len[i+1]==arr_of_len[i] and i==len(arr_of_len)-2):
#         counter1+=1
#         print("the sum of string " + str(arr_of_len[i]) + " is:" + str(counter1))
#     elif arr_of_len[i+1]==arr_of_len[i]:
#         counter1 += 1
#     elif i==len(arr_of_len)-2 and arr_of_len[i+1]!=arr_of_len[i] :
#         print("the sum of string "+str(arr_of_len[i])+" is:"+str(counter1))
#         print("the sum of string " + str(arr_of_len[i+1]) + " is: 1" )
#     else:
#         print("the sum of string " + str(arr_of_len[i]) + " is:" + str(counter1))
#         counter1=1
#     i+=1

#7
# end_of_input=False
# while not end_of_input:
#     numbers=int(input("enter numbers: "))
#     if(numbers%2!=0):
#         end_of_input=True
# print("finish")

#8
# number=int(input("enter number: "))
# counter=0
# while number!=0:
#     number= number//10
#     counter+=1
#
# print(counter)

#9
# number=int(input("enter number: "))
# num=str(number)
# num=num[::-1]
# print(num)
#
# number=int(input("enter number: "))
# num=0
# num=number
# while number!=0:
#     num=num%10
#     number=number//10
#     print(num, end='')
#     num=number%10

# import random
# end_of_input=False
#
# random_num = random.randint(1, 100)
# while not end_of_input:
#     number = input("guess the number: ")
#     if number=='exit':
#         end_of_input=True
#     elif int(number)==random_num:
#         print("exactly right!")
#     elif int(number)>random_num:
#         print('too high')
#     elif int(number)<random_num:
#         print('too low')
