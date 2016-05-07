def fibos(upto):
    r = [1]
    a, b = 1, 1
    while b <= upto:
        r.append(b)
        a, b = b, a+b
    return r


def zaek(n):
    fibs = fibos(n)

    def nearest_f(n):
        for i, f in enumerate(fibs):
            if f > n:
                return fibs[i-1]
            elif f == n:
                return n
        return fibs[-1]        
    
    r = []
    while n>0:
        d = nearest_f(n)
        n -= d
        r.append(d)
    
    return r

for i in xrange(1, 100):
    print i, zaek(i)

def z_len(upto):
    prev_fibo = 1
    next_fibo = 2
    
    z = [1]

    for n in xrange(2, upto + 1):        
        if n == next_fibo:
            prev_fibo, next_fibo = next_fibo, prev_fibo + next_fibo            
            # print prev_fibo, next_fibo
            next_z = 1
        else:
            # print n - prev_fibo
            next_z = 1 + z[n - prev_fibo - 1]
        
        z.append(next_z)

    return z



def plotstuff():
    from matplotlib import pyplot as plt
    # zz = z_len(10**2-1)
    zz = z_len(35)
    zzs = [zz[0]]
    for i in xrange(1, len(zz)):
        zzs.append(zz[i] - zz[i-1])
    # print sum(zz)
    x = range(1, 1+len(zz))
    plt.plot(x, zz, 'r.-')
    # plt.plot(x, zzs, 'b.-')
    plt.show()

# plotstuff()


# print 10**16 
# print 14472334024676221 - 10**16 
# print len(str(abs(10**16 - 14472334024676221)))