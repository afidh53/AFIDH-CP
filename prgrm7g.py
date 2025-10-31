area1=lambda x:x*x
area2=lambda x,y:x*y
area3=lambda x,y:0.5*x*y
a=int(input("enter the length of the square:"))
print("Area of the square is",area1(a))
l=int(input("enter the length of the rectangle:"))
w=int(input("enter the width of the rectangle:"))
print("Area of the rectangle is",area2(1,w))
h=int(input("enter the height of the triangle:"))
b=int(input("enter the base of the triangle:"))
print("Area of the triangle is",area3(b,h))
