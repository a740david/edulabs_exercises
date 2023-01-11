#ex1
# number=int(input("insert numbur: "))
# if(number>=0 and number<10):
#     digits=1
# elif(number>=10 and number<100):
#     digits = 2
# elif (number >= 100 and number < 1000):
#     digits = 3
# elif (number >= 1000 and number <= 4000):
#     digits = 4
# print(digits)

#ex2
# numbers1=int(input("insert number1: "))
# numbers2=int(input("insert number2: "))
# numbers3=int(input("insert number3: "))
# if(numbers1>numbers2 and numbers1>numbers3):
#   sum3=numbers1
#   sum2=numbers2
#   sum1=numbers3
# if(numbers1>numbers2 and numbers1<numbers3):
#   sum3=numbers3
#   sum2=numbers1
#   sum1=numbers2
# if(numbers1<numbers2 and numbers2>numbers3):
#   sum3=numbers2
#   sum2=numbers1
#   sum1=numbers3
# if(numbers1<numbers2 and numbers2<numbers3):
#   sum3=numbers3
#   sum2=numbers2
#   sum1=numbers1
# if(numbers1<numbers3 and numbers3<numbers2) :
#   sum3=numbers2
#   sum2=numbers3
#   sum1=numbers1
# print(sum1,sum2,sum3)

#ex3
# age=int(input("enter your age: "))
# height=int(input(("enter your height: ")))
# if(18>age>8 and height>=115):
#     print('You can ride')
# elif(age>18):
#     height>=100
#     print('You can ride')
# else:
#     print("You cannot ride")

#ex4
# player1=input("enter Rock-Paper-Scissors: ")
# player2=input("enter Rock-Paper-Scissors: ")
# if(player1=="rock" and player2=="ruls"):
#     print("winer player1")
# elif(player1=="ruls"and player2=="rock"):
#     print("winer player2")
# if(player1=="scissors"and player2=="paper"):
#     print("winer player1")
# elif(player1=="paper" and player2=="scissors"):
#     print("winer player2")
# if(player1=="paper"and player2=="rock"):
#     print("winer player1")
# elif (player1 == "rock" and player2 == "paper"):
#     print("winer player2")

#ex5
# dd=input("enter a day: ")
# mm=input("enter a month: ")
# year=input("enter a year: ")
# if(mm=="12" or mm=="01" or mm=="03"):
#     print("winter , 31 days")
# elif(mm=="02"):
#     print("winter , 28 days")
# elif(mm=="06"):
#     print("summer , 30 days")
# elif(mm=="07" or mm=="08"):
#     print("summer 31 days")
# elif (mm == "09" or mm == "11"):
#     print("autumn , 30 days")
# elif( mm == "10"):
#     print("autumn , 31 days")
# elif (mm == "04"):
#     print("spring 30 days")
# elif(mm == "05" ):
#     print("spring 31 days")

#ex6
# year=int(input("is_leap_year: "))
# leap= (year%4 ==0)and (year%100!=0 or year%400 ==0)
# print(leap)

# ex8
# temperature=int(input("what is the temperature outside: "))
# if(temperature>15):
#      weather= input("what's the weather like outside: ")
#      if(weather=="sun"):
#          print("sun")
# else:
#     weather = input("what's the weather like outside: ")
#     if(weather=="rain"):
#         print("rain")
#     elif(weather=="snow"):
#         print("snow")
# #
# ex9
# salery= int(input("enter a salery: "))
#
# if(salery>0 and salery<77401):
#       salery= salery*0.9
#       print(salery)
# elif(salery>77401 and salery<110880):
#       salery = salery * 0.86
#       print(salery)
# elif(salery > 110880 and salery < 178080):
#       salery = salery * 0.80
#       print(salery)
# elif(salery > 178080 and salery < 247440):
#       salery = salery * 0.69
#       print(salery)
# elif (salery > 247440 and salery < 514920):
#       salery = salery * 0.65
#       print(salery)

# books
#
# books_histori=int(input("enter a books_histori: "))
# books_sciencefiction=int(input("enter a books_sciencefiction: "))
# books_comics=int(input("enter a books_comics: "))
#
# if(books_sciencefiction>=3):
#    total_s= books_sciencefiction*58
#    Discount_books_sciencfiction=total_s*0.90
#
# if(books_histori>=3):
#     total_b= books_histori*24
#     Discount_books_histori=total_b
#     Discount_books_histori=-24
#
# if(books_comics>=0):
#     total_c=books_comics*32
#
# Discount_total_books=(Discount_books_histori+Discount_books_sciencfiction+total_c)
# total_books=(books_histori*24)+(books_comics*32)+(books_sciencefiction*58)
# if(Discount_total_books>300):
#     Discount_total_books=-20
#     print('Discount_total_books', Discount_total_books)
#     print('total_books', total_books)
# elif(Discount_total_books<=300):
#     print('Discount_total_books', Discount_total_books)
#     print('total_books', total_books)

# user=input("Insert a storage unit/kb/mb/gb/tb: ")
# if(user=="kb"):
#     number=int(input("Insert a degree of storage: "))
#     convert=input("Why do you want to convert: ")
#     if(convert=="mb"):
#         result=number*10**-4*9.77
#         print(result)
