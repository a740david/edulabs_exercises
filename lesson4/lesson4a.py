#1
# def sum(list):
#  sum_arr=0
#  for i in list:
#      sum_arr+=i
#  return sum_arr
# arr=[21.5,40]
# print(sum(arr))

#2
# def multiply(numbers):
#     total = 1
#     for x in numbers:
#         total *= x
#     return total
# print(multiply((1,2,3)))

#3
# def max_num(num1,num2,num3):
#     x=max(num1,num2,num3)
#     return x
# num1=int(input("enter the number: "))
# num2=int(input("enter the number: "))
# num3=int(input("enter the number: "))
# print(max_num(num1,num2,num3))

#4
# def factorial(number):
#     total=1
#     for i in range(1,number+1):
#         total*=i
#     return total
# number=int(input("enter the number: "))
# print(factorial(number))

#5
# def func(number):
#  arr=[]
#  for i in number:
#     if i not in arr:
#       arr.append(i)
#  return tuple(arr)
# arr=(12, 3, 4, 12, 7, 3, 8)
# print(func(arr))

#6
# def func(number):
#
#  for i in number:
#      if number.count(i)>1:
#          number.remove(i)
#  return number
# arr=[12, 3, 4, 12, 7, 3, 8]
# print(func(arr))

#7
# def func(arr):
#     numbers=[]
#     for i in arr:
#         if i%2==0:
#             numbers.append(i)
#     return numbers
#
# arr=[3,9,4,1,2]
# print(func(arr))

#8

# def isPerfect(n):
#     sum = 1
#
#     i = 2
#     while i * i <= n:
#         if n % i == 0:
#             sum = sum + i + n / i
#         i += 1
#
#     return (True if sum == n and n != 1 else False)
# number=[6,87,496,5]
#
# n = 2
# for n in number:
#     if isPerfect(n):
#         print(n, " is a perfect number")

