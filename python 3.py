# factorial using recursion

def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
num=5
if num <0:
    print("neg num")
elif num ==0:
    print(" The factorial of 0 is 1")
else:
    print("The factorial of",num,"is",fact(num))

# To find a factorial

num=int(input("Enter the num:"))

factorial= 1
if num<0:
    print("Not exist for negative num")
elif num==0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
        print("The factorial of",num,"is",factorial)

# find area

def square(x):
    return x*x
def tri(a,b,c):
   s = (a + b + c) / 2
   return (s*(s-a)*(s-b)*(s-c)) ** 0.5
def rect(l,b1):
    return l*b1

x=int(input("enter value to find area of square:"))

print("Enter the sides of triangle")
a=int(input("Side A:"))
b=int(input("Side B:"))
c=int(input("Side C:"))

print("Enter the value to find the area of rectangle")
l=int(input("Enter the length:"))
b1=int(input("Enter the breadth:"))

print("area of square is:", square(x))
print("area of triangle is", tri(a,b,c))
print("area of rectangle is:", rect(l,b1))

# multilevel inheritance

class car:
    def engine(self):
        print("Engine is running")

class brake(car):
    def stop(self):
        print("Brake applied car is stopped")

class stop(brake):
    def park(self):
        print("car is now parked")

c = stop()
c.engine()
c.stop()
c.park()


# multiple inheritance

class father():
    def driving(self):
        print("father likes driving")
class mother():
    def cooking(self):
        print("mother like cooking")
class child(father,mother):
    def playing(self):
        print("child likes playing")
c=child()
c.driving()
c.cooking()
c.playing()


# sum of natural numbers

num = int(input("Enter a number"))
if num < 0:
    print("Enter a number")
else:
    sum = 0
    while(num > 0):
        sum += num
        num -= 1
        print("the sum is",sum)

