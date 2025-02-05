#pattern-3
def hollpy():
    n=int(input("Enter a number:"))
    for i in range(1,n+1):
        if (i==1 or i==n):
           print(' '*(n-i)+"*"*(2*i-1))
        else:
           print(' '*(n-i)+"*"+' '*(i*2-3)+"*")

hollpy()
