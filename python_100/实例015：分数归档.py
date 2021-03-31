#题目 利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
#我觉得这道题的难度，在于让我对编程还有信心学下去！
print("请输入学习成绩：",end="")
score = int(input())
if score>=90:
    print("该同学等级为A！")
elif (score>=60)and(score<90):
    print("该同学等级为B！")
else:
    print("该同学等级为c！")
