age=25
height=8.34
complex_num=3+4j


#Area of a triangle
base=20
height=10
area=0.5*base*height
print(area)


#Perimeter of a circle
a=5
b=4
c=3
perimeter=(a+b+c)
print(perimeter)

#Area and perimeter of a rectangle
length=12
width=14
area=length*width
perimeter=2*(length+width)
print(area)
print(perimeter)


#Area of a circumference of a circle
radius=14
pi=3.14
area=pi*radius**2
circumference=2*pi*radius
print(area)
print(circumference)

#y=2x-2
x=1
slope=2
x_intercept=1
y_intercept=-2
print(slope)
print(x_intercept)
print(y_intercept)

# #slope and Euclidean distance
# x1,y1=2,2
# x2,y2=6,10
# slope=(y2-y1)/(x2-x1)
# distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
# print(slope)
# print(distance)

#y = x^2 + 6x + 9
for x in range (-10,11):
    y=x**2+6*x+9
    print(f"x={x},y={y}")

print('python'>'dragon')

print('on' in'python' and 'on' in 'dragon')

print('on' not in 'python' and '0n' not in 'dragon')

sentence="I hope this course is not full of jargon"
print('jargon' in sentence)

print('on' not in 'python' and 'on' not in 'dragon')

#convert length of python to float and string
text="python"
length=len(text)
print(float(length))
print(str(length))

#check if even
num=6
print("Even" if num%2==0 else "Odd")

#floor division and int cast check
print(int(7/3)==int(2.7))

#type check
print(type('10')==type(10))



