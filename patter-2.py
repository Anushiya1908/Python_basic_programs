#hourglass
#consist of inverted pyramid and pyramid
n=int(input("Enter a number:"))
for i in range(n,0,-1):
    print(" "*(n-i)+"* "*i)
for j in range(2,n+1):
    print(' '*(n-j)+"* "*j)
