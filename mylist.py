n=int(input('number of n: '))
a=2*n
b=0
i=0

mylist = []
while i<a:
    b+=i
    print(i)
    mylist.append(str(i))
    i+=2 

s = "+"
seq = mylist

c = s.join(seq)

print('\n number of n even number: \n', c, "=", b)