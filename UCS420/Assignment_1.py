print("Hello World")


print("Harshita")
print("harshita")
print("Harshita")


a=100
b=20
c=a+b
print(c)


s1="Hello"
s2="How are u"
result = s1+" "+s2
print(result)


a= 22
b=17
result= str(a) +" "+str(b)
print(result)


a=10
b=20
c=30
sum=a+b+c
print("the sum is:",sum)


a="how"
b="are"
c="youu"
result= a+" "+b+" "+c
print(result)


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
result = num1+num2+num3
print(result)

for i in range(11):
    print(i)


i = 1
while i <= 10:
    print(i)
    i += 1

for i in range(1,11):
    print(5*i)


n= int(input("enter the value: "))
for i in range(1,11):
    print(n*i)

n= int(input("enter n: "))
sum=0
for i in range(n+1):
    sum=sum+1
    print(sum)

a= int(input("enter the first: "))
b= int(input("enter the second: "))
if a>b:
    print(a,">",b)
else:
        print(a,"<",b)

age=28
if age>18:
    print(age,">",18)
else:
    print(age,"<",18)


n= int(input("enter the number: "))
if n%2==0:
    print("even")
else:
    print("odd")

n = int(input("enter the number: "))
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")

a= input("enter first string: ")
b= input("enter second string: ")
if a==b:
    print("a==b")
elif a>=b:
    print("a>b")
else:
    print("a<b")

n1 = int(input("enter the number: "))
n2 = int(input("enter the number: "))
n3 = int(input("enter the number: "))
m= max(n1,n2,n3)
print(m)

n = int(input("enter the number: "))
total_sum= 0
for i in range(1,n+1):
    if i%7==0 and i%9==0:
        total_sum+=i
        print(total_sum)


n = int(input("Enter the number: ")) 
total_sum = 0 
for num in range(2, n + 1):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            break
    else:
        total_sum += num 

print(total_sum)

