temp=0
n=int(input("enter the no. "))
def Factorial_of_no(n):
    if n==0 or n==1:
        return 1
    else:
        return n * Factorial_of_no(n-1)

result = Factorial_of_no(n)
print("Factorial of a given no. is", result)

