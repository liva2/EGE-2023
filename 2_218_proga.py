# ((z → y) ∧ (¬ x → w)) → ((z ≡ w) ∨ (y ∧ ¬ x)).

from itertools import permutations
import itertools

print('ЕГЭ_2 задача 218')
print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((z <= y) and ((not x) <= w)) <= ((z == w) or (y and not x))) == 0:
                    print(x, y, z, w)
print('*************************************************************************')
a = [[1, -1, 1, 1], [-1, 0, 0, 0], [-1, -1, 0, -1]]
#a = [[1, -1, 1, 1]]
u = 0
d1 =[]
d2 = []
d3 = []
for d in a:
    n = d.count(-1)
    u = u + 1
    for x in range(0,int('1'*n,2)+1):
        t =bin(x)[2:]
        if (n - len(t)) !=0:
            t  = '0'* (n - len(t)) + bin(x)[2:]
            #print(t)
        else:
            t = bin(x)[2:]
            #print(t)
        f = list(map(int, t))
        s= d.copy()


        for j in range(len(s)):
            if s[j] ==-1:
                s[j] = f[0]

                del f[0]
        print('s = ', s)
        per = itertools.permutations('xyzw', 4)

        for val in per:
            r = list(val)
            #print(r)

            if (((s[r.index('z')]<= s[r.index('y')]) and ((not s[r.index('x')]) <= s[r.index('w')])) <= ((s[r.index('z')] == s[r.index('w')]) or (s[r.index('y')] and not s[r.index('x')]))) == 0:
                print(r)
                if u ==1:
                    d1.append(r)
                if u == 2:
                    d2.append(r)
                if u ==3:
                    d3.append(r)

    print('------------')

print(d1)
print('1111111111111111')
print(d2)
print('2222222222222222')
print(d3)
print('3333333333333333')
c = []
for i in d1:
    for j in d2:
        for g in d3:
            if i == j and i == g and j == g:
                c.append(i)
                break
print(c)