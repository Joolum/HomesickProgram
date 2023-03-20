import math

def q1(x):
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
        print("Area is : %.2f" % area)
    else:
        print("It is not a triangle!")

def q3():
    odd = 0
    even = 0
    for i in range(1, 101):
        if i % 2 != 0:
            odd += i
        else:
            even += i
    print('Odd is: %d. Even is %d.' % (odd, even))

print(q1(2))
q2(3, 4, 5)
q3()
for i in range(0, 3):
    print(q1(1))
