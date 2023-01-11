#1
# number=int(input("enter the number: "))
# k = number - 1
#
# for i in range(0, number):
#     for j in range(0, k):
#         print(end=" ")
#
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("\r")

#2
# number=int(input("enter the number: "))
# for i in range(0,number):
#     for j in range(0,i+1):
#         print("*", end="")
#     print("\r")

#3

# number=int(input("enter the number: "))
#
# for i in range(number):
#     for j in range(number-i,-1,-1):
#         print(" ", end="")
#     for j in range(1 + i ):
#            print('*', end='')
#     print("\r")
#4
# number=int(input("enter the number: "))
#
# for i in range(number):
#     for j in range(number - i - 1):
#         print(' ', end='')
#     for j in range(2 * i + 1):
#         print('*', end='')
#     print()
#
# # downward pyramid
# for i in range(number - 1):
#     for j in range(i + 1):
#         print(' ', end='')
#     for j in range(2*(number - i - 1) - 1):
#         print('*', end='')
#     print()

#5
# number=int(input("enter the number: "))
# for i in range(0,number):
#     for j in range(0,number-i):
#         print("*", end="")
#     print("\r")

#6
# number=int(input("enter the number: "))
#
# for i in range(number):
#     for j in range(number-i,-1,-1):
#         print(" ", end="")
#     for j in range(1 + i):
#            print('*', end='')
#     print("\r")
#7
# number = int(input("enter the number: "))
# i = 0
# while i <= number - 1:
#     j = 0
#     while j < i:
#         # display space
#         print('', end=' ')
#         j += 1
#     k = i
#     while k <= number - 1:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1
#8
# number=int(input("enter the number: "))
#
# i = number
# while i >= 1:
#     j = number
#     while j > i:
#         print(' ', end=' ')
#         j -= 1
#     k = 1
#     while k <= i:
#         print('*', end=' ')
#         k += 1
#     print()
#     i -= 1

#9

#
# number=int(input("enter the number: "))
# for i in range(1,number):
#     for j in range(1,i+1):
#         print("* ", end="")
#     print("\r")
# for i in range(0,number):
#     for j in range(0,number-i):
#         print("* ", end="")
#     print("\r")

#10
# number=int(input("enter the number: "))
# i = 1
# while i <= number:
#     j = i
#     while j < number:
#         print(' ', end=' ')
#         j += 1
#     k = 1
#     while k <= i:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1
#
# i = number
# while i >= 1:
#     j = i
#     while j <= number:
#         print(' ', end=' ')
#         j += 1
#     k = 1
#     while k < i:
#         print('*', end=' ')
#         k += 1
#     print('')
#     i -= 1

#11
# number = int(input("enter the number: "))
# i = 0
# while i <= number - 1:
#     j = 0
#     while j < i:
#         # display space
#         print('', end=' ')
#         j += 1
#     k = i
#     while k <= number - 1:
#         print('*', end=' ')
#         k += 1
#     print()
#     i += 1
# k = number - 1
#
# for i in range(0, number):
#     for j in range(0, k):
#         print(end=" ")
#
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("\r")

#13
# number = int(input("enter the number: "))
# i = 1
# while i < number:
#     j = number
#     while j > i:
#         print(' ', end=' ')
#         j -= 1
#     print('*', end=' ')
#     k = 1
#     while k < 2 * (i - 1):
#         print(' ', end=' ')
#         k += 1
#     if i == 1 :
#         print()
#     else:
#         print('*')
#     i += 1
# for j in range(2*number-1):
#     print('* ',end='')

#14
# number = int(input("enter the number: "))
# for i in range(2*number-2):
#     print('* ',end='')
#
#
# i = number
# while i >= 1:
#     j = number
#     while j > i:
#         print(' ', end=' ')
#         j -= 1
#     print('*', end=' ')
#     k = 1
#     while k < 2 * (i - 1):
#         print(' ', end=' ')
#         k += 1
#     if i == 1:
#         print()
#     else:
#         print('*')
#     i -= 1

#15
# number = int(input("enter the number: "))
# i = 1
# while i < number:
#     j = number
#     while j > i:
#         print(' ', end=' ')
#         j -= 1
#     print('*', end=' ')
#     k = 1
#     while k < 2 * (i - 1):
#         print(' ', end=' ')
#         k += 1
#     if i == 1 :
#         print()
#     else:
#         print('*')
#     i += 1
# i = number
# while i >= 1:
#     j = number
#     while j > i:
#         print(' ', end=' ')
#         j -= 1
#     print('*', end=' ')
#     k = 1
#     while k < 2 * (i - 1):
#         print(' ', end=' ')
#         k += 1
#     if i == 1:
#         print()
#     else:
#         print('*')
#     i -= 1

#1
# number=int(input("enter the number: "))
# for i in range(0,number):
#     for j in range(1,i+2):
#         print(j, end="")
#     print("\r")

#2
# number=int(input("enter the number: "))
# counter=0
# for i in range(0,number):
#     for j in range(1,i+2):
#         counter += 1
#         print(counter," ", end="")
#     print("\r")

