
#ex1
# def climbStairs( n: int) -> int:
#
#  first=0
#  second=1
#  for i in range(n):
#     num=first+second
#     first = second
#     second = num
#  return num
#
#
#
# n=int(input('insert n: '))
# print(climbStairs(n))

#ex2

#
# def romanToInt(s: str) -> int:
#         list_s=list(s)
#         dict={'I':1,
#               'V':5,
#               'X':10,
#               'L':50,
#               'C':100,
#               'D':500,
#               'M':1000
#         }
#         counter=0
#         list__s=[]
#         for i in list_s:
#                 if i in dict.keys():
#                     counter+=dict[i]
#         return counter
#
#
# s = input('insert s: ')
# print(romanToInt(s))