#armstron or not
#sum of digit to the power of number of digit is equal to the same number as input
print("To find if the given number is Armstrong or not")  
def armstrong(n):
    temp = n
    length_of_number = 0
    while temp > 0:
        temp //= 10
        length_of_number += 1
    temp = n
    sum_of_powers = 0
    while temp > 0:
        digit = temp % 10
        # Get the last digit
        sum_of_powers += digit ** length_of_number
        # Add the digit raised to the power
        temp //= 10
        # Remove the last digit integer division
    
    # Return whether the sum is equal to the original number
    return sum_of_powers == n

# Test the function
n = int(input("Enter a number: "))
if armstrong(n):
    print("The given number is Armstrong.")
else:
    print("The given number is not Armstrong.")
