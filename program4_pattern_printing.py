#patterns-star
#programs for practice
#1.right angled triangle
def righttri():
    n=int(input("Enter a number:"))
    for i in range(1,n+1):
        print("*"*i)#print sting * according to the number given as row

#2.left triangle
def lefttri():
    n=int(input("Enter a number:"))
    for i in range(1,n+1):
        print(' '*(n-i)+"*"*i)#reduce the space value to form left angled triangle


#3,pyramid
def pyramid():
    n=int(input("Enter a number:"))
    for i in range(1,n+1):
        print(' '*(n-i)+"* "*i+' '*(n-i))#consist of space in both sides and string in the middle to form pyramid

#4.Diamond
def diamond():
    n=int(input("Enter a number:"))
    for i in range(1,n+1):
        print(' '*(n-i)+"* "*i+' '*(n-i))#indicate number of row and same as pyramid
    for j in range(n-1,0,-1):
        print(' '*(n-j)+"* "*j+' '*(n-j))#print inverted pyramid

lefttri()
righttri()
pyramid()
diamond()                    
