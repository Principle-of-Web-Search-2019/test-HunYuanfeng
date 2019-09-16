# 心血来潮自己设计24点游戏,输入4个合法的数，自动找到可以组合出24的情况

# 排列组合
class InputError(Exception):
    def __str__(self):
        return "输入格式有误!请重新输入。"

ari = ['+','-','*','/']

# 组合
def MyPermutations(num_list):
    seen = []    
    result = []
    L = range(len(num_list))
    for i in L:
          for j in L:
                for k in L:
                    for w in L:
                        if len(set((i,j,k,w))) == 4:
                            result.append(list((i,j,k,w)))
    for each in result:
        temp = [num_list[each[0]],num_list[each[1]],num_list[each[2]],num_list[each[3]]]
        if temp not in seen:
            seen.append(temp)
        
    return seen

    
    
def CombineNA(s, p):
    return ([list(zip(s,p))[i][j] for i in range(len(s)) for j in range(len(list(zip(s,p))[0]))])

def ExPandBrackets(ExListNew, e):
    eNew = e[:] #拷贝列表
    eNew.insert(0,'(')
    eNew.insert(4,')')
    eNew.insert(6,'(')
    eNew.insert(12,')')
    ExListNew.append(eNew)
    for N in [0,2,4]:
        for i in range(2,4):
            eNew = e[:] #拷贝列表
            eNew.insert(N,'(')
            eNew.insert(N + i * 2,')')
            ExListNew.append(eNew)

def Find24(s):
    AriList, ExList, ResultList = [], [], []
    
    
    for i in ari:
        for j in ari:
            for k in ari:
                AriList.append([i,j,k,''])
    
    for e in AriList:
        ExList.append(CombineNA(s, e)[:-1])
        
    ExListNew = ExList[:]
    for i in range(len(ExList)):
        ExPandBrackets(ExListNew, ExList[i])
    
    for k in ExListNew:
        driv = "".join(k)
        try:
            y = eval(driv)
        except ZeroDivisionError:
            continue
        equ = driv + '=' + str(int(y))
        #print(equ)
        if y == 24:
            ResultList.append(equ)
    return list(set(ResultList))

def main():
    print("欢迎进入24点游戏作弊器~")
    while 1:
        try:        
            alist = input("请输入4个整数,数的范围是1-13,每个数以空格隔开:\n")
            s = alist.split(" ")[:4]
            #s = [int(i) for i in alist.split(" ")]
            if len(s) == 4 and (0 < e < 14 and type(e) == int for e in s):
                break
            else:
                raise InputError
        except InputError as e:
            print(e)
    print("输入完成,请等待结果。。。\n")
    
    #s = ['1', '2' ,'3','4']
    #print(s)
    tempList = MyPermutations(s)
    #print(tempList)
    Final = []
    for each in tempList:
        t = Find24(each)
        Final.append(t)
    result = sum(Final, [])
    if len(result) > 0:
        print("O(∩_∩)O找到啦~\n")
        for each in result:
            print(each.replace('*', 'x'))
    else:
        print("o(╥﹏╥)o没有合适的结果。")
    print("\n游戏结束。")

if __name__ == '__main__':
    main()
    input('Press Enter to exit...')
