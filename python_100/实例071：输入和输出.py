#题目 编写input()和output()函数输入，输出5个学生的数据记录。
#出现TypeError: input() missing 2 required positional arguments: 'stu' and 'n'，是因为我把函数名字与内置函数取一致了！不能定义为input或output
student = []
n = 5
for i in range(n):
    student.append(['',''])
def input_stu(stu,n):
    for i in range(n):
        print("请输入第",i+1,"个学生的名字：",end="")
        stu[i][0] = input()
        print("请输入第", i+1, "个学生的性别：",end="")
        stu[i][1] = input()
def output_stu(stu,n):
    for i in range(n):
        print("第",i+1,"个学生的名字：",end="")
        print(stu[i][0])
        print("请输入第", i+1, "个学生的性别：",end="")
        print(stu[i][1])
if __name__ == '__main__':
    input_stu(student,n)
    #print (student)
    output_stu(student,n)
#参考答案
# N = 3
# student = []
# for i in range(5):
#     student.append(['','',[]])
#
# def input_stu(stu):
#     for i in range(N):
#         stu[i][0] = input('input student num:\n')
#         stu[i][1] = input('input student name:\n')
#         for j in range(3):
#             stu[i][2].append(int(input('score:\n')))
#
# def output_stu(stu):
#     for i in range(N):
#         print ('%-6s%-10s' % ( stu[i][0],stu[i][1] ))
#         for j in range(3):
#             print ('%-8d' % stu[i][2][j])
#
# if __name__ == '__main__':
#     input_stu(student)
#     print (student)
#     output_stu(student)