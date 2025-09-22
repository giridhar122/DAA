def q(a):
    if len(a) <= 1:
        return a
    p = a[len(a) // 2]
    l = [x for x in a if x < p]
    m = [x for x in a if x == p]
    r = [x for x in a if x > p]
    return q(l) + m + q(r)

a = [10, 7, 8, 9, 1, 5]
s = q(a)
print(s)
