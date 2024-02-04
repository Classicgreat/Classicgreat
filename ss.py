def ss(n,k):
    alf="0123456789abcdefghijklmnopqrstuvwxyz"
    b=""
    while n!=0:
        b=alf[n%k]+b
        n//=k
    return b
def ss_ten(n,k):
    b=0
    for i in range(len(n)):
        b+=int(n[-(i+1)])*k**i
    return b
a=ss_ten("14",5)
b=ss_ten("24",7)
x=ss(12345623741761419094,36)
print(x)