import random

t1="开始游戏"
t2="结束游戏"
print(t1.center(50,"*"))
data1=[]
money=int(input("输入投入的金额："))
print("你现在余额为：%d元"%money)
while 1:
    '''中奖号码生成'''
    for i in range(4):
        n = random.choice([0, 1])
        data1.append(n)
    data = ''
    for i in data1:
        data = data + str(i)

    '''余额不足的情况下'''
    if money<2:
        print("你的余额不足，请充值")
        m=input("输入投入的金额：")
        if int(m)==0 or int(m)<=0:
            print("\n输入错误，请重新输入")
        else:
            money=int(m)

    '''余额充足的情况下，买几张彩票'''
    n = 0
    while money >= 2:
        j=int(input("每张彩票价格为2元，请输入购买彩票数量:"))
        n = j
        if money-j*2<0:
            print("购买后余额不足，请重新输入")
        else:
            money = money - j * 2
            print("你现在余额为：%d元" % money)
            break

    '''输入并购买j张彩票'''
    f = []
    k=0
    print("提示：中奖数据有4位数，每位数为0或者1")
    print("请猜测中奖数据：（输入的数字为0或1）")
    while k <n:
        n2=input("第%d张彩票"% (k+1))
        f.append(n2)
        k += 1
    
    '''买的彩票和中奖彩票比较'''
    k=0
    print("\n你猜测的数据为：", f)
    while k < n:
        if str(f[k])==str(data):
            print("中奖数字为：",data)
            print("恭喜你中大奖啦")
            money=money+j*100
            print("你现在余额为：%d元" % money)
        else:
            print("中奖数字为：", data , "而你的中奖数字为", f[k])
            print("没有中奖，请继续加油")
        k += 1

    '''询问是否退出''' 
    con = input("请问还要继续么？结束请输入no,继续请任意输入字符：")
    if con=="no":
        break
    data1=[]
    
'''模拟结束，显示余额'''  
print(t2.center(50,"*"))
print("你的余额为：%d元"%money)