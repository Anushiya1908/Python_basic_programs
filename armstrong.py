#armstrong number
def armstrong():
    n=int(input("Enter a number: "))
    temp=n
    sumi=0
    a=str(n)
    b=len(a)
    while(temp>0):
        dig = temp %10
        sumi += dig**b
        temp //=10
    print(sumi)
    if (sumi==n):
        print("The given number is an armstrong number")
    else:
        print("The given number is not an armstrong number")
armstrong()
