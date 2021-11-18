1. Arithmetic operation

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

a=int(input("enter value of a:"))
b=int(input("enter value of b:"))

print("sum of a and b is:", add(a,b))
print("sub of a and b is:", sub(a,b))
print("mul of a and b is:", mul(a,b))
print("div of a and b is:", div(a,b))

2. Binary search

def binary(arr, start,end,x):
    if end >= start:
        mid = start + (end-start)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary(arr,start,mid-1,x)
        else:
            return binary (arr,mid+1,end,x)
    else:
        return-1
arr=sorted(['r','o','s','y'])
x='r'
result=binary(arr,0,len(arr)-1,x)
if result !=-1:
    print("ele is at"+str(result))
else:
    print("not found")


3. Table of 2

def table(n):
    return lambda a:a*n
n=2
b=table(n)
for i in range(1,11):
    print(n,"X",i,"=",b(i))

4. factors using list append

def getfact(n):
    factors=[]

    for i in range(1, n+1):
        if n%i==0:
            factors.append(i)

    return factors

print(getfact(256))

5. square root

def fun(n):
    return n ** 0.5

n=(int(input("enter the number to find the square root ")))
print(fun(n))

6. to check prime number

num= int(input("enter num"))
if num > 1:
    for i in range(2,num):
        if(num % i) == 0:
            print(num,"is not a prime number")
            break
    else:
        print(num,"is a prime number")
