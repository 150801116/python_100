#题目 两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
# 已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
#眼睛都能看出来的一道题，我居然反复尝试反复不对，反思啊


b = ['x','y','z']

for i in b:       #i表示a对战的可能性
    for j in b:   #j表示b对战的可能性
        for k in b:  #k表示c对战的可能性
            if(i=='x')or(k=='x')or(k=='z'):    #跳过a对战x,c对战x,z的可能
                continue
            elif len(set((i,j,k)))==3:   #set只能传一个iterable的内容,所以有两个括号（（i,j,k）），不加括号就是三个内容了
                print("a:%s,b:%s,c:%s"%(i,j,k))


#参考答案
print("答案输出")
a=set(['x','y','z'])
b=set(['x','y','z'])
c=set(['x','y','z'])
c-=set(('x','z'))   #c自减，减去z不对战的可能
a-=set('x')         #a自减，减去x不对战的可能
for i in a:
    for j in b:
        for k in c:
            if len(set((i,j,k)))==3:  #运用了集合的不可重复性
                print('a:%s,b:%s,c:%s'%(i,j,k))







