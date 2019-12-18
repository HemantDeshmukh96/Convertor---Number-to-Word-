no=int(input("Enter any Four digit Number :"))
num1=no//1000
def part1(num):
    if (num==1):
        return "One"
    elif (num == 2):
        return "Two"
    elif (num == 3):
        return "Three"
    elif (num == 4):
        return "Four"
    elif (num == 5):
        return "Five"
    elif (num == 6):
        return "Six"
    elif (num == 7):
        return "Seven"
    elif (num == 8):
        return "Eight"
    elif (num==9):
        return "Nine"
    else:
        return " "
def part2(num):
    if (num >= 90):
        return "Ninty"
    elif(num >= 80):
        return  "Eighty"
    elif (num >= 70):
        return "Seventy"
    elif (num >= 60):
        return("Sixty")
    elif (num >= 50):
        return("Fifty")
    elif (num >= 40):
        return("Fourty")
    elif (num >= 30):
        return("Thirty")
    elif (num >= 20):
        return("Twenty")
def part3(num):
    if (num==10):
        return "Ten"
    if (num == 11):
        return "Eleven"
    elif (num == 12):
        return "Twelve"
    elif (num==13):
        return "Thirteen"
    elif (num == 14):
        return "Fourteen"
    elif (num == 15):
        return "Fifteen"
    elif (num == 16):
        return "Sixteen"
    elif (num == 17):
        return "Seventeen"
    elif (num == 18):
        return "Eigthteen"
    elif (num == 19):
        return "Nineteen"
num2=(no%1000)//100
n1=part1(num1)
n2=part1(num2)
num3=((no%1000)%100)
n3=part2(num3)
if no>=1000:
    print(n1,"Thousand",end=" ")
if no>=100:
    print(n2,"Hundred",end=" ")
if num3>=20:
    print(n3,end=" ")
    num4 = (((no % 1000) % 100) % 10)
    n4 = part1(num4)
    if num4 < 10:
        print(n4, end="")
if num3>=10 and num3<=19:
    n5=part3(num3)
    print(n5,end="")
else:
    print(" ")

# ANOTHER METHOD TO PROCESS IF CONDITIONS
