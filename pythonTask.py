import math

def squre(side):
    squre_Side = side
    squre_Area = squre_Side ** 2
    squre_Girth = squre_Side * 4
    print ('The squre side is %d' % squre_Side)
    print ('The squre area is %d' % squre_Area)
    print ('The squre girth is %d' % squre_Girth)
    
def exchangeNumber(firstNum,secondNum):
    print('First number is: %d. Second number is %d.' % (firstNum,secondNum))
    swap = firstNum
    firstNum = secondNum
    secondNum = swap
    print('Exchanged first number is: %d. Exchanged second number is %d' % (firstNum,secondNum))

def triangle(s1,s2,s3):
    p = float((s1 + s2 + s3) / 2)
    area = (p * (p - s1) * (p - s2) * (p - s3)) ** 0.5
    print('The triangle area is {:.2f}' .format(area))

def judgeYear(year):
    print((year % 4 == 0 & year % 100 != 0) or (year % 400 == 0))

def mathPractice(x):
    x = float(x)
    y = math.sin(x) + 2 * math.sqrt(x + math.exp(4) - pow((x + 1), 3))
    y = round(y, 2)
    print('y=', y)

squre(5)
print('-----------------------')
triangle(3,4,5)
print('-----------------------')
exchangeNumber(2,5)
print('-----------------------')
judgeYear(2023)
print('-----------------------')
mathPractice(2)
