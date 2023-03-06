# #com@6 : to print difference between even and odd numbers in a given number
n = int(input("enter a number:"))
se=0
so=0
while(n!=0):
    r = n%10
    if(r%2==0):
        se=se+r
    else:
        so = so+r
    n = n//10
print("difference:",abs(so-se))
