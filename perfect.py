
#perfect number
#check whether the sum of factors of number are equal to number
def perfect():
    n=int(input("Enter a number to find whether it is perfect number or not:"))
    sumi=0
    for i in range(1,n):
        if(n%i==0):
            sumi += i
    if(n==sumi):
        print("Perfect square")
    else:
        print("Not a perfect square")
perfect()
