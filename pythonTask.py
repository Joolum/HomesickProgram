import math

def squre(side):
    squre_Side = side
    squre_Area = math.sqrt(squre_Side)
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

def tringleSqure(s1,s2,s3):
    
