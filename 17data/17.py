#178
f = open('17-4.txt', 'r')
count = 0
y = list(map(int,(f.readlines())))
#print(sorted(y))
mini = 10001
f.close()
maxi=-1
for x in y:
    k = 0
    for d in range(2, x//2 + 1):
        if  x% d == 0 and d in [2,3,5,7]:
            k = k + 1
            if k > 2:
                break
    if k == 2:
        count = count +1
        if x > maxi:
            maxi=x
        if  x< mini:
            mini = x

print(count,mini, maxi,mini+ maxi )
