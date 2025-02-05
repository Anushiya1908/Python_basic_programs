#fizzbuzz
#if the given number is divisible by 3 and 5 return fizzbuzz only 3 fizz and only 5 buzz
def fizzbuzz():
    n=int(input("Enter a starting value: "))
    m=int(input("Enter an ending value: "))
    str=[]

    for i in range(n,m+1):
          if(i%3==0 and i%5==0):
             str.append("FizzBuzz")
          elif(i%3==0):
              str.append("Fizz")
          elif(i%5==0):
              str.append("Buzz")
          else:
              str.append(i)
    print(str)    
fizzbuzz()
