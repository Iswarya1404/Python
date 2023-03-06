# to display no of camdies left and available
n=10
print("no of candies available:",n)
k=int(input("enter no of candies needed:"))
if(k>5 or k==0):
    print("INVALID INPUT")
else:
    n=n-k;
    print("no of candies sold:",k)
    print("no of candies left:",n)
    


