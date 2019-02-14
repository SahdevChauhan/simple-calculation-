#simple calculater program in python
import sys

def add(x,y):
    return x + y
   
def sub(x,y):
    return x - y
   
def div(x,y):
    return x / y
   
def mult(x,y):
    return x * y
   
print('select operation:')
print('1.Add')
print('2.Subtraction')
print('3.Division')
print('4.multiplication')
while True:
    
    choice=input("enter choice(1/2/3/4):")
    if choice == '1':
        
        a=int(input('enter the first value: '))
        b=int(input('enter the second value: '))
        total = int(a) + int(b)
        print(a,'+', b ,'=', add(a,b))
        f  = open("Addition.txt", "a+")
        f.write(" First number : {}\n Second number :  {}\n Total :  {} ".format(a,b,str(total)))
        f.close()
 
    elif choice == '2':
        a=int(input('enter the first value: '))
        b=int(input('enter the second value: '))
        total = int(a) + int(b)
        print(a,'-', b , '=', sub(a,b))
        f  = open("subraction.txt", "a+")
        f.write(" First number : {}\n Second number :  {}\n Total :  {} ".format(a,b,str(total)))
        f.close()
      
    elif choice == '3':
        a=int(input('enter the first value: '))
        b=int(input('enter the second value: '))
        total = int(a) + int(b)
        print(a,'/', b ,'=', div(a,b))
        f  = open("Division.txt", "a+")
        f.write(" First number : {}\n Second number :  {}\n Total :  {} ".format(a,b,str(total)))
        f.close() 
 
      
    elif choice == '4':
        a=int(input('enter the first value: '))
        b=int(input('enter the second value: '))
        total = int(a) + int(b)
        print(a,'*', b ,'=', mult(a,b))
        f  = open("Multiplication.txt", "a+")
        f.write(" First number : {}\n Second number :  {}\n Total :  {} ".format(a,b,str(total)))
        f.close() 
          
    elif choice == '0':
        sys.exit()
        
    else:
        print('invalid option........')
