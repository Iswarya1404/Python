# write a program to print the nth term in the following series
#series: 1 1 2 3 4 9 8 27 16 81 32 243 64 729 128 2187

n = int(input())
if(n%2==0):
    n = n//2
    print(3**(n-1))
else:
    n = n//2 + 1
    print(2**(n-1))

