import math

def q1(x):
<<<<<<< HEAD
    if x < 0:
        return x * x
    elif 0 <= x <= 5:
        return 3 * x - 5
    elif x >= 5:
        return 0.5 * x - 2

def q2(a, b, c):
    if a + b > c > 0 and a + c > b > 0 and b + c > a > 0:
        print("It is a triangle!")
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
=======
    if x<0:
        return x*x
    elif 0<=x<5:
        return 3*x-5
    elif x>=5:
        return x/2-2

def q2(a,b,c):
    if a+b>c and a+c>b and b+c>a and a>0 and b>0 and c>0:
        print("It is a triangle!")
        p = (a+b+c)/2
        area = math.sqrt(p*(p-a)*(p-b)*(p-c))
>>>>>>> 40148f856996e66eab2a48a5c0e71e878078f220
        print("Area is : %.2f" % area)
    else:
        print("It is not a triangle!")

def q3():
<<<<<<< HEAD
    odd = 0
    even = 0
    for i in range(1, 101):
        if i % 2 != 0:
            odd += i
        else:
            even += i
    print('Odd is: %d. Even is %d.' % (odd, even))

print(q1(2))
print('>>>>>>>>')
q2(3, 4, 5)
print('>>>>>>>>')
q3()
print('>>>>>>>>')
for i in range(0, 3):
    print(q1(1))
=======
    for i in range(1,101):
        odd = 1
        even = 0
        if i%2!=0:
            odd+=i
        else:
            even+=i

        print('Odd is: %d. Even is %d.' % (odd,even))

q1(2)
q2(3,4,5)
q3()
>>>>>>> 40148f856996e66eab2a48a5c0e71e878078f220
