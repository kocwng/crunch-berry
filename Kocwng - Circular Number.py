import math

def isprime(n):
    for i in range(3, int(math.pow(n, 0.5))+2, 2):
        if n % i == 0:
            return False
    return True

#Rotations
def rotations(prime):
    s = str(prime)
    r = [prime]
    for n in range(1, len(s)):
        r.append(int(s[n:] + s[:n]))
    return list(set(r))

#Circular Rotations
def cr(prime):
    s = str(prime)
    #bilangan prima mengandung 0, 2, 4, 5, 6, 8 tidak circular.
    if any(i in s for i in '024568'):
        return []
    else:
        r = rotations(prime)
        for n in r:
            if isprime(n) == False:
                return []
        return r

#Primes
def p(n):
    a = [True] * n
    a[0] = a[1] = False
    for i in range(2, int(math.sqrt(n))+1, 1):
        if a[i]:
            j = i**2
            while j < n:
                a[j] = False
                j = j + i
    for x in range(len(a)):
        if a[x]:
            yield x

#Circular Primes
def cp(limit):
    cp_list = []
    for i in p(limit):
        if i > 9 and i not in cp_list:
            r = cr(i)
            if len(r) > 1:
                print (r)
                cp_list.extend(r)
            elif len(r) == 1:
                print (i)
                cp_list.append(i)
        elif i==2 or i==3 or i==5 or i==7:
            print (i)
            cp_list.append(i)
    return cp_list

print('insert the limit!')

limit = int(input('\nlimit = '))

print('\n')

print ('\nNumber of circular primes under {} is {}'.format(limit, len(cp(limit))))
