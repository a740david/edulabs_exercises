
#1
# number= int(input("enter of number: "))
# sum=0
# for i in range(number+1):
#     sum+=i
# print(sum)

#2
# list=[89,4,9,34,2,5]
# temp=0
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if(list[i]>list[j]):
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp
# print(list[0])

#3
# list=[89,4,9,34,2,5]
# temp=0
# for i in range(len(list)):
#     for j in range(i+1,len(list)):
#         if(list[i]>list[j]):
#             temp=list[i]
#             list[i]=list[j]
#             list[j]=temp
# print(list[1])

#4
# list=[89,4,9,34,2,5]
#
# for i in list[::-1]:
#     print(i)

#5

# counter_autmen=0
# counter_winter=0
# counter_sprint=0
# counter_summer=0
#
# autumn=["09","10","11"]
# winter=["12","01","02"]
# sprint=["03","04","05"]
# summer=["06","07","08"]
#
# date_autumn=[]
# date_winter=[]
# date_sprint=[]
# date_summer=[]
#
# for i in range(10):
#  year=input("enter the year: ")
#  month=input("enter the month: ")
#  day=input("enter the day: ")
#  for i in autumn:
#     if i==month:
#      counter_autmen+=1
#      date_autumn.append(year + '.' + month + '.' + day)
#
#  for i in winter:
#     if i==month:
#      counter_winter+=1
#      date_winter.append(year + '.' + month + '.' + day)
#
#  for i in sprint:
#     if i==month:
#      counter_sprint+=1
#      date_sprint.append(year + '.' + month + '.' + day)
#
#  for i in summer:
#     if i==month:
#      counter_summer+=1
#      date_summer.append(year + '.' + month + '.' + day)
#
# print(f"You entered "+str(counter_autmen) + f" dates in autmen: ")
# for i in date_autumn:
#     print(i)
# print(f"You entered "+str(counter_winter) + f" dates in winter: ")
# for i in date_winter:
#     print(i)
# print(f"You entered "+str(counter_sprint) + f" dates in sprint: ")
# for i in date_sprint:
#     print(i)
# print(f"You entered "+str(counter_summer) + f" dates in summer: ")
# for i in date_summer:
#     print(i)

#6
# num=int(input("enter the number: "))
#
# factorial = 1
#
# # check if the number is negative, positive or zero
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#    print("The factorial of",num,"is",factorial)

#7
# num=int(input("enter the number: "))
# for i in range(1,11):
#     print(i*num)

#8
# rows=int(input("enter the num_rows: "))
# for i in range(1,rows+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print(" ")

#9

# prime numbers are greater than 1

# bool=False
# for i in range(2, num+1):
#     for j in range(2,i):
#            if(i%j==0):
#                bool=True
#     if( not bool):
#         print(i)
#
#     bool = False

#10
# rows = input("Enter the number of rows: ")
#
# for i in range(0, int(rows)):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print(" ")
# for i in range(int(rows) , 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")
