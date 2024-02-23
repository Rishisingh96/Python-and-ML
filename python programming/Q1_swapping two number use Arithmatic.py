#Python3 program to
#swap two number
#without using temporary variables
x=input("Enter the two number for swaping: for x =")
x=int(x)
y=input("Enter the two number for swaping: for y =")
y=int(y)
x=x*y;
y=x // y; # // 
x = x // y;
print("After swappiing : x =", x,"y=`",y);

