#1
# num=0
# first=0
# second=1
# print(first)
# print(second)
# for i in range(7):
#     num=first+second
#     print(num)
#     first = second
#     second = num

#2
# arr=[0,1,0,0,0,0,0,0,0,0]
# for i in range(2,10):
#     arr[i]=arr[i-1]+arr[i-2]
#
# print(arr)

# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# my_list1=[]
# for i in range(1,10,2):
#      my_list1.append(my_list[i])
# print(my_list1)

#3
# cities = ['New York', 'Kyiv', 'Paris', 'London', 'Tel Aviv']
# countries = ['USA', 'Ukraine', 'France', 'UK', 'Israel']
#
# for i in range(0,5):
#     print(countries[i]+'-'+ cities[i])

#4
# cube=int(input("enter the number: "))
# for i in range(1,cube+1):
#     print('Current Number is: ' + str(i)  + 'end the cube is '+ str(i**3))

#5
# number=int(input("enter the number: "))
# sum=[2]
# counter=0
#
# for i in range(1, number):
#     sum.append(2)
#
# for i in range(1,number):
#     for j in range(i,number):
#         sum[j]=sum[j]*10+2
#
# sum1=0
# for i in sum:
#     sum1=sum1+int(i)
# print(sum1)

#6
# names = ['Moshe', 'Orly', 'David', 'Jack', 'Ofer', 'James']
#
# names_dr=[]
# for i in range(0,6):
#      names_dr.append('D"r '+names[i])
#
# print(names_dr)

#7
# number=int(input('enter the number: '))
# squares=[]
# for i in range(1,number+1):
#     squares.append(i*i)
# print(squares)

#8
# list1=[20,"htg",456]
# newlist=[]
# for i in list1:
#    if(type(i)==int):
#       newlist.append(i)
#
# print(newlist)

#9
# list=[2,4,5,7,9]
# sum_even=0
# sum_odd=0
# for i in list:
#    if( i%2==0):
#       sum_even+=1
#
#    else:
#       sum_odd+=1
# print(sum_even)
# print(sum_odd)

#10
# list=['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
#
# for i in list:
#   if(type(i)==int):
#       print(str(i)+"-int")

#11
# for i in range(0,50):
#      if(i%3==0 and i%5==0):
#         print( "fizzBuzz")
#      elif(i%5==0):
#         print("Fizz")
#      elif(i%3==0):
#         print("Buzz")
#      else:
#          print(i)

#12
# rows=int(input("enter of number rows: "))
# columns=int(input("enter of number columns: "))
# rows1=""
# for i in range(0,rows):
#     rows1="$"
#     for i in range(0,columns):
#        print(rows1, end='')
#     print(" ")

#13
# number= int(input("enter of number: "))
# for i in range(1,number +1):
#      for j in range(i):
#          print(i,end="")
#      print(" ")
