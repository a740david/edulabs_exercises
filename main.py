



# text=input("enter a string: ")
# spilt_text=text.split(" ")
# print(spilt_text)
# print("spilt_text[0]=",spilt_text[0])
# if (len(spilt_text)==2):

#operotor in
# grades=[90,95,97,85]
# print(50 in grades)
# print(97 in grades)

# arr=input("enter a string: ")
# x=len(arr)
# y=arr.count(" ")+1
# z=arr.count("a")
# t=arr.count("o")
# print(x)
# print(y)
# print(z)
# print(t)
#

# end_of_input = False
# temp_max = None
# while not end_of_input:
#     i = input("Insert num or $ to finish: ")
#     if i == '$':
#         end_of_input = True
#     else:
#         num = int(i)
#         if temp_max is None:
#             temp_max = num
#         if num > temp_max:
#             temp_max = num
# print("MAx num", t

# mm=[]
# winter = ["01", "02", "12"]
# summer = ["03", "04", "05"]
# spring = ["06", "07", "08"]
# autumn = ["09", "10", "11"]
#
# for i in range(10):
#     date = input("enter a date: ")
#     date.split("."[1])
#     if(date[winter]==winter[i]):
#          print()
#
#

# drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', 'coffee', 'tea']
#
# filter_drinks_i=[]
#
# for drink in drinks:
#     if "i" not in drink:
#         filter_drinks_i.append(drink)
# print(filter_drinks_i)



# def is_31_days_month(month,year):
#     month_list=(1,3,5,7,8,10,12)
#     if month in month_list:
#         return 31
#     else:
#         return 29
#
# print(is_31_days_month(1,1999))

# prefix="Dr"
# def apppend_dr(neam):
#     print(prefix)
#     ret_val = "Dr."
#     return ret_val



# def sum_list(list_of_number):
#     sum=0
#     for i in list_of_number:
#         sum+=i
#     return sum
#
# print(sum_list([1,3,4]))

# def string_f(name):
#         return name[::-1]
# print(string_f("abcde"))

# def f(number,ranger):
#      for i in ranger:
#         if number in ranger:
#                 return True
#         return False
#
# print(f(2 , [1,2,6]))

# def parmeter(string_ ):
#         sum_uppers=0
#         sum_lowers=0
#         for i in range(len(string_)):
#               if(string_[i].isupper()):
#                       sum_uppers=sum_uppers+1
#               else:
#                       sum_lowers=sum_lowers+1
#         return sum_lowers,sum_uppers
# l,u=parmeter("abstryueCD")
# print("sum_uppers: "+str(u))
# print("sum_lowers: "+ str(l))



#set

# colors_2 = ['red', 'White', 'BLUE','white', 'Red',
#             'sky blue', 'purple', 'orange with white straps']
# #
# def f(colors: list[str]) ->set:
#     ret_val=set()
#     for color in colors:
#         ret_val.add(color.lower())
#     return ret_val
#
# print(f(colors_2))

# def analyze_str(word:str)->tuple[int,str,str]:
#     return len(word) ,word.upper(),word.lower()
#
# ret_val=analyze_str('Hello')
# word_len,word_u,word_l=analyze_str("Hello")
# print(word_len,word_u,word_l)
# def f(colors: list[str], num:int) ->set:
#     print(colors)
#     print(num)
#     num=50
#     colors[0] ="bl"
#     print("inside func")
#
#
# my_num=100
# f(colors_2, my_num)
# print(my_num)
# print(colors_2)


# 1
# def second_largest(list_of_numbers):
#
#     list_of_numbers.sort()
#     for i in list_of_numbers:
#         if (list_of_numbers[i-1] != list_of_numbers[i-2]):
#             return list_of_numbers[-2]
#         elif (list_of_numbers[i-1] == list_of_numbers[i-2]):
#             return  list_of_numbers[-3]
#         else:
#             return None
# print(second_largest([54, -1, 45, 987, 5, 2, 65, 7, 12]))

#2
# def fizz_buzz(number):
#     i=0
#     ret_val=''
#     for i in len(range(number)):
#     return ret_val
#
# number = int(input("enter number: "))
# print(fizz_buzz(number))

