a = 1
count = 0

if a == 1:
    b = 105700
    c = 122700
else:
    b = 57
    c = 57

d = e = f = g = h = 0

while True:
    f = 1
    d = 2
    while True:
        e = 2
        if b % d == 0 and b > (b // d) > 1:
            f = 0
        e = b
        count += (b - 2)

        d += 1
        if d == b:
            break
    if f == 0:
        #print (a, b, c, d, e, f, g, h)
        h += 1
    if b == c:
        break
    b += 17

print(h)
print(count)
