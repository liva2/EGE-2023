#задача 95
a = open('26-95.txt')
n = int(next(a).rstrip())
x = {}
for i in range(n):
     b, c = map(int, next(a).rstrip().split())
     x[b] = sorted(x.get(b, []) + [c])
#print(x)
mini_pod = 0
domm = {}
for i, j in x.items():
     f = 0
     if len(j) >= 3:
          for y in range(len(j)-2):
               if j[y + 1] - j[y] == j[y + 2] - j[y + 1]:
                    mini_pod = j[y] - 1
                    f = 1
               elif (j[y + 1] - j[y])  == 1 and (j[y+2] - j[y+1]) == 2:
                    mini_pod = j[y + 1] + 1
                    f = 1
               elif (j[y + 2] - j[y + 1]) == 1 and (j[y + 1] - j[y]) == 2:
                    mini_pod = j[y + 1] - 1
                    f = 1
               if f==1:
                    domm[i] = domm.get(i, []) + [mini_pod]
                    break
     else:
          continue
print(len(domm), *list(max(domm.items()))[1])

#*****************************************************************************************************

# задача 96

# a = open('26-96.txt')
#
# n = int(next(a).rstrip())
# print(n)
# x = {}
# for i in range(n):
#     b, c = map(int,next(a).rstrip().split())
#     if i == 0:
#         print(b,c)
#     x[c] = x.get(c,[]) + [b//10]
# #print(sorted(x.items(),key=lambda t:t[0],reverse=True))
# m = 1
# for i, j in x.items():
#     if len(j)> m:
#         m = len(j)
#         keyy = i
#         dolg = j
#
# #for t in range(len(dolg)):
#     #dolg[t] = dolg[t]//10
# #print(sorted(dolg))
# print(keyy, len(set(dolg)))
# '''
# a = [123,234,-3,5,123]
# b = [407,34,52,52,407]
# d=dict(zip(b,a))
# print(d)
# '''
