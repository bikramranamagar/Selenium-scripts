a=int(input("enter your first number: "))
b=int(input("enter your second number: "))
symbol=input("enter your operator: ")
#addition
def sum():
    print("the sum is: ",a+b)
#subtraction
def subtract():
    print("the subtrtaction is: ",a-b)
#multiplication
def mul():
    print("the product is: ", a*b)
#division
def div():
    if b==0:
        print("number cant divide with zero")
    else:
        print("the divison is :", a/b)
#operations with symbol
if symbol=="+":
    sum()
elif symbol == "-":
    subtract()
elif symbol=="*":
    mul()
elif symbol=="/":
    div()
else:
    print("enter valid operatior")