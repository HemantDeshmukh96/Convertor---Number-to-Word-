num=(input("Enter a four digit Number :"))
n=int(num)
n1=n//1000
n2=n%1000
n3=n2//100
n4=n2%100
n5=n4//10
n6=n4%10
if (n1==1):
    print("One Thousand",end=' ')
elif(n1==2):
    print("Two Thousand",end=' ')
elif(n1==3):
    print("Three Thousand",end=' ')
elif(n1==4):
    print("Four Thousand",end=' ')
elif(n1==5):
    print("Five Thousand",end=' ')
elif(n1==6):
    print("Six Thousand",end=' ')
elif(n1==7):
    print("Seven Thousand",end=' ')
elif(n1==8):
    print("Eight Thousand",end=' ')
elif(n1==9):
    print("Nine Thousand",end=' ')
else:
    print("",end=' ')
if (n3==1):
    print("One Hundred",end=' ')
elif(n3==2):
    print("Two Hundred",end=' ')
elif(n3==3):
    print("Three Hundred",end=' ')
elif(n3==4):
    print("Four Hundred",end=' ')
elif(n3==5):
    print("Five Hundred",end=' ')
elif(n3==6):
    print("Six Hundred",end=' ')
elif(n3==7):
    print("Seven Hundred",end=' ')
elif(n3==8):
    print("Eight Hundred",end=' ')
elif(n3==9):
    print("Nine Hundred",end=' ')
else:
    print("",end=' ')
if(n4>=90 and n4<=99):
    print("Ninty",end=' ')
elif(n4>=80 and n4<=89):
    print("Eighty",end=' ')
elif(n4>=70 and n4<=79):
    print("Seventy",end=' ')
elif(n4>=60 and n4<=69):
    print("Sixty",end=' ')
elif(n4>=50 and n4<=59):
    print("Fifty",end=' ')
elif(n4>=40 and n4<=49):
    print("Fourty",end=' ')
elif(n4>=30 and n4<=39):
    print("Thirty",end=' ')
elif(n4>=20 and n4<=29):
    print("Twenty",end=' ')
if(n4>=11)and(n4<=19):
    if(n4==11):
        print("Eleven",end=' ')
    elif(n4==12):
        print("Twelve",end=' ')
    elif(n4==13):
        print("Thirteen",end=' ')
    elif(n4==14):
        print("Fourteen",end=' ')
    elif(n4==15):
        print("Fifteen",end=' ')
    elif(n4==16):
        print("Sixteen",end=' ')
    elif(n4==17):
        print("Seventeen",end=' ')
    elif(n4==18):
        print("Eigthteen",end=' ')
    elif(n4==19):
        print("Nineteen",end=' ')
else:
    print("",end=' ')
if(n4>=20 or n4<=9):
    if (n6==1):
        print("One",end=' ')
    elif(n6==2):
        print("Two",end=' ')
    elif(n6==3):
        print("Three",end=' ')
    elif(n6==4):
        print("Four",end=' ')
    elif(n6==5):
        print("Five",end=' ')
    elif(n6==6):
        print("Six",end=' ')
    elif(n6==7):
        print("Seven",end=' ')
    elif(n6==8):
        print("Eight",end=' ')
    elif(n6==9):
        print("Nine",end=' ')
    else:
        print("",end=' ')