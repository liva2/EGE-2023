# 218 ((z → y) ∧ (¬ x → w)) → ((z ≡ w) ∨ (y ∧ ¬ x)).
print('ЕГЭ_2 задача 218')
print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((z <= y) and ((not x) <= w)) <= ((z == w) or (y and not x))) == 0:
                    print(x, y, z, w)

#229 ((x → z) → y) ∨ ¬w
print('ЕГЭ_2 задача 229')
print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((x <= z) <= y) or (not w)) == 0:
                    print(x, y, z, w) 

#231 (¬x → y) ∧ (¬y ≡ z) ∧ w
print('ЕГЭ_2 задача 231')
print('x,y,z,w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if (((not x) <= y) and ((not y) == z) and w) == 1:
                    print(x, y, z, w)
