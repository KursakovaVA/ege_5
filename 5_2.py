for N in range(1,1000):
    N = bin(N)[2:]
    w = int("110110",2)
    if N.count("1")%2==0:
        N += "1"
    else:
        N += "0"
    if N.count("1")%2==0:
        N += "1"
    else:
        N += "0"
    if int(N,2) > w:
        print(int(N,2))
        break