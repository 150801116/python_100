# 题目 有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
flag = 1
n = 10
list = []
for i in range(n):
    list.append(i + 1)
# print(list)
s = list


t = 0
while flag:
    if len(s) == 1:
        flag = 0
        # print(s)
    for i in s.copy():
        t += 1
        if t == 3:
            s.remove(i)
            t = 0
    print(s)

# 参考答案
# if __name__ == '__main__':
#     nmax = 50
#     n = int(input('请输入总人数:'))
#     num = []
#     for i in range(n):
#         num.append(i + 1)
#
#     i = 0
#     k = 0
#     m = 0
#
#     while m < n - 1:
#         if num[i] != 0 : k += 1
#         if k == 3:
#             num[i] = 0
#             k = 0
#             m += 1
#         i += 1
#         if i == n : i = 0
#
#     i = 0
#     while num[i] == 0: i += 1
#     print(num[i])
