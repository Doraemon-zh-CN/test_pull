while True:
    import random
    punches = ['石头','布','剪刀'] #列表
    computer = random.choice(punches)

# 输入
    user_choice = input('请出拳：（石头、剪刀、布）\n')

    while user_choice not in punches:   #返回布尔值，真或者假
        print('输入有误，请重新选择')
        user_choice = input('请继续输入：')

#出拳过程
    print('开始比较')
    print('电脑的选择是：',computer)
    print('我的选择是：',user_choice)

#结果
    print('---结果---')
    if user_choice == computer:
        print('平局')
        continue
    elif (user_choice == '石头' and computer == '剪刀') or (user_choice == '剪刀' and computer == '布') or (user_choice =='布'and computer == '石头'):
        print('你赢了')
        break
    else: print('你输了')
