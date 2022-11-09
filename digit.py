import random
from itertools import combinations
from itertools import permutations
#1
# max = 1
# for x in range(100, 1000):
#     s = sum(list(map(int,str(x))))
#     if x % 100 != 0 and x % s ==0 and x // s > max:
#         max=x // s
#
#         print(x)
#4
# a = []
# for i in range(10,100):
#     a.append(i)
# y = list(combinations(a, 4))
# #print(y)
# for j in range(len(y)):
#     if ((y[j][0] + y[j][2]) / (y[j][1] + y[j][3]))== 7/19:
#         print(y[j])
#         break
#20

# a = []
# f=0
# for i in range(1000,10000):
#     s =(list(map(int,str(i))))
#     if 0 not in s:
#         f= 1
#         y = set(permutations(s, 4))
#         #print(y)
#         t = list(y)
#         for j in t:
#             if t[0][0] == t[0][1]+ t[0][2] + t[0][3]:
#                 a.append(i)
# t = set(a)
# t1 = list(t)
# print(t1)
# if 6222 in t1:
#     print('+')
# r = list(combinations(t1, 2))
# print(r)
# for j in range(len(r)):
#     if abs((r[j][0] - r[j][1])) == 3:
#         print(r[j])
#41
# k = 30
# s = 0
# a = []
# for x in range(2454):
#     if x % 10 == 2 or x% 10 == 6:
#         a.append(x)
# r = list(combinations(a, k))
# print(r)

# for i in range(len(r)):
#     if sum(r[i]) == 2454:
#         print(r[i])
#20

a = []
f=0
for i in range(1,2014):
   a.append(i)
r = list(combinations(a, 2))
#print(r)
print('**********************')

for x in range(len(r)):
    s1 = sum(list(map(int, str(r[x][0]))))
    s2 = sum(list(map(int, str(r[x][1]))))
    if s1==s2 and r[x][0]+r[x][1]==2014:
        print(r[x][0],r[x][1])
        break