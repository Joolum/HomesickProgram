def squre(side):
    squre_Side = side
    squre_Area = squre_Side ** 2
    squre_Girth = squre_Side * 4
    print ('The squre side is %d' squre_Side)
    print ('The squre area is %d' squre_Area)
    print ('The squre girth is %d' squre_Girth)

def exchangeNumber(firstNum,secondNum):
    swap = firstNum
    firstNum = secondNum
    secondNum = swap
    print('First number is: %d. Second number is %d.' (firstNum,secondNum))
    print('Exchanged first number is: %d. Exchanged second number is %d'(firstNum,secondNum))

def triangle(s1,s2,s3):
    p = (s1 + s2 + s3) / 2
    area = (p * (p - s1) * (p - s2) * (p - s3)) ** 0.5
    print('The triangle area is %d' area)