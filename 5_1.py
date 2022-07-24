m=10000
for N in range(1,100):
    R = bin(N)[2:]
    if R==R[::-1]:
        R += '11'
        if int(R,2)>180:
            m = min(m,N)
    else:
        R = '1'+R
        if int(R,2)>180:
            m = min(m,N)
print(m)
            