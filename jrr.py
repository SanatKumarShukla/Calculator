def expo(a,b):
    r=a
    for i in range(b-1):
        r=r*a
    return r
def facto(a):
    r=a
    while a!=1:
        r=r*(a-1)
        a=a-1
    return r
def sin(a):
    r=a
    for i in range(1,15):
        r=r+((expo(-1,i))*((expo(a,2*i+1))/facto((2*i+1))))
    return r
def cos(a):
    r=1
    for i in range(1,15):
        r=r+((expo(-1,i))*(expo(a,2*i))/facto((2*i)))
    return r
def tan(a):
    if cos(a)==0:
        print("inf")
    else:
        r=sin(a)/cos(a)
    return r
def sec(a):
    if cos(a)==0:
        print("inf")
    else:
        r=1/cos(a)
    return r
def cosec(a):
    if sin(a)==0:
        print("inf")
    else:
        r=1/sin(a)
    return r
def cot(a):
    if tan(a)==0:
        print("inf")
    else:
        r=1/tan(a)
    return r
    
#-----------MAIN-------------
print("Welcome to Calculator")
while True:
    print("Enter the required operation:")
    print("1] Arathematic(+,-,*,/) \n2] Trignometric \n3] exponential")
    i=int(input("Enter choice(1,2,3):"))
    if i==1:

        a=float(input("Enter first no.:"))
        b=float(input("Enter second no.:"))
        print("Available choices: \n1] Addition \n2] Subraction \n3] Multiplication \n4] Division")
        e=int(input("Enter choice:"))
        if e==1:
            print(a,"+",b,"=",a+b)
        elif e==2:
            print(a,"-",b,"=",a-b)
        elif e==3:
            print(a,"*",b,"=",a*b)
        elif e==4:
            if b==0:
                print("inf")
            else:
                print(a,"/",b,"=",a/b)
    if i==2:
        a=float(input("Enter the angle(in degree):"))
        print("Available choices: \n1] Sin \n2] Cos \n3] Tan \n4] Cot \n5] Sec \n6] Cosec")
        e=int(input("Enter choice:"))
        b=a*3.1415926/180
        if e==1:
            print(sin(b))
        elif e==2:
            print(cos(b))
        elif e==3:
            print(tan(b))
        elif e==4:
            print(cot(b))
        elif e==5:
            print(sec(b))
        elif e==6:
            print(cosec(b))
    if i==3:
        print("Available choices: \n1] Exponential \n2] Factorial")
        e=int(input("Enter choice:"))
        if e==1:
            a=float(input("Enter base:"))
            b=int(input("Enter power:"))
            print(expo(a,b))
        elif e==2:
            a=int(input("Enter a number:"))
            print(facto(a))
    t=input("want to enter more:(y/n)")
    if t=="n":
        break




     