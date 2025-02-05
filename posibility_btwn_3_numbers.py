#all possibilities between 3 numbers
a=int(input("Enter a number:"))
b=int(input("Enter a number:"))
c=int(input("Enter a number:"))
if(a == b and a==c):
    print("All are equal")
else:
    print("all are not equal")
    if(a==b and a!=c):
        print("A is equal to b but not c")
        if(a>c):
            print("a and b are greater than c")
        else:
            print("C is greater number than a and b")
    elif(b==c and b!=a):
        print("b is equal to c but not a")
        if(b>a):
            print("b and c are greater than a")
        else:
            print("a is greater than b and c")
    elif(c==a and c!=b):
        print("c is equal to a but not b")
        if(c>b):
            print("a and c are greater than b")
    elif(a>c and a>b):
        print("a is the greatest")
    elif(b>a and b>c):
        print("B is greatest")
    else:
        print("c is the greatest")
