def calci():
    ch=(int)(input('1) Addition\n2) Subtraction\n3) Multiplication\n4) Division\n5) Modulus\n'))
    a=int(input('Enter the value for a: '))
    b=int(input('Enter the value for b: '))
    if ch==1:
        res=a+b
        print('Sum= ',res)
    elif ch==2:
        res=a-b
        print('Difference= ',res)
    elif ch==3:
        res=a*b
        print('Product: ',res)
    elif ch==4:
        res=a//b
        print('Quotient= ',res)
    elif ch==5:
        res=a%b
        print('Remainder: ',res)
    else:
        print('Invalid Choice')
    return 0


