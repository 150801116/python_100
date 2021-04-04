#题目 字符串排序。
#依旧可以用sort()
l=['baaa','aaab','aaba','aaaa','abaa']
#l.sort()
print(l)
#不用sort()版本
for i in range(len(l)-1):
    if l[i+1]<l[i]:
        l[i],l[i+1]=l[i+1],l[i]
print(l)