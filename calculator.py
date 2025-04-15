def sum(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0 :
        return
    return a/b
def modulus(a,b):
    return a%b
while True :
     print('A SIMPLE CALCULATOR')
     a=float(input('enter first number '))
     b=float(input('enter second number '))
     choice=input('chose the operation you want to perform(+,-,*,%,/)')
     if choice=='exist':
        print("existing calculator")
        break


     if choice=='+':
       print( sum(a,b))
     elif choice=='-':
      print(subtract(a,b))
     elif choice=='*':
      print( multiply(a,b))
     elif choice=='/':
      print( divide(a,b))
     elif choice=='%':
      print(modulus(a,b))
     else : print('Invalid operation')
     again=input('do you want to perform another function(y for yes , n for no)').lower()
     if(again!='y'):
        break

