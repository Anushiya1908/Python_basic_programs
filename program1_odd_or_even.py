#odd or even
#aim is to find whether the number is odd or even

def odd_even():
    n=int(input("Enter a number:"))
    print("To check the number from user is odd or even")
    #the if statement checks the condition and gets executed only when condition is true if not else block will get executed
    if(n%2==0):
         print(n,"is even")
    else:
         print(n,"is odd")


odd_even()
