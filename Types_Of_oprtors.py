#arithmatic operator

a=5
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)  #remainder
print(a**b)  #a^b


#relational operator
a=50
b=40

print(a==b) #flase
print(a != b) #true
print(a >= b) #true
print(a <= b) #false
print(a > b) #true
print(a < b) #false


#assignment operator

num=10
num+=10
print("num ",num)
num-=5
print("num ",num)
num*=10
print("num ",num)
num/=7
print("num ",num)
num%=5
print("num ",num)
num**=5
print("num ",num)


#logical operator
a=20
b=10
print(not False)
print(not (a>b))

v1=True
v2=True
print("And operation is ",v1 and v2)
print("Or operation is ",v1 or v2)
print("or operation is ",(a>b) and (a==b))


#type conversion
a=4

b=5.4

sum=a+b
print(sum)
d="4"
c=int(d)
print(type(a))

e=3.14
e=str(e)

print(type(e))
