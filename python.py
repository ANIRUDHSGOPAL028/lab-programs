a =int(input("enter 3 numbers"))
b= int (input(""))
c= int (input(""))
if(a>=b and a>=c):
    print("a and b is big ",(a+b)/2)
elif(b>=c and b>=a):
    if(a>c):
        print("b and a is big",(a+b)/2)    
else:
    if(a>b):
        print("a and c is big",(a+c)/2)
    else:
        print("c and b is big ",(c+b)/2)   
                                              