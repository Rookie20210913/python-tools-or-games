import random

def revise(a):
    if len(a)==1:
        temp=a
        a='0'
        return a+temp
    else:
        return a

num1=str(random.randint(0,99))
num1=revise(num1)
print("正確答案為:{}\n目前猜測次數剩餘 3 次\n\n下方開始猜數字".format(num1))
check=False
times=0
while(check!=True):
    num2 = input("輸入兩位數:")
    num2 = revise(num2)
    if (num1[0]==num2[0] and num1[1]!=num2[1])or (num1[0]!=num2[0] and num1[1]==num2[1]):
        print("1A")
    elif num1[0]==num2[1] and num1[1]==num2[0]:
        print("2B")
    elif (num1[0]==num2[1] or num1[1]==num2[0]):
        print('1B')
    elif (num1[0]!=num2[0] or num1[1]!=num2[1]):
        print("全錯")
    # elif (num1[0]==num2[0] and num1[1]==num2[1]):
    else:
        print('\nYou win')
        check=True

    times+=1
    print("已猜測 {} 次，剩餘 {} 次機會".format(times,3-times))
    if times==3 and num1!=num2:
        check=True
        print("你輸了")
