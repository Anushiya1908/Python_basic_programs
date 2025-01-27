#sum of digits
def sum_of_digits():
    sum = 0
    temp=n
    #copying or temporary variable
    while temp>0:
        digit=temp%10
        #returns the remainder
        sum += digit
        #sum of the remainder value stored in sum
        temp //=10
        #contains quotient value
    print(sum,"is the sum of digit")

    
n=int(input("Enter a number:"))
sum_of_digits()
        
