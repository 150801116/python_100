#题目 画图，学用circle画圆形。
#很明显，这个circle我又一次没用过，自卑啊。。。
from tkinter import *
canvas = Canvas(width=800,height=600,bg="yellow") #设置画布控件，大小800X600，背景颜色huangse
canvas.pack(expand=YES,fill=BOTH)
k = 1
j = 1
for i in range(26):
    canvas.create_oval(310-k,250-k,310+k,250+k,width=1)
    k +=j
    j +=0.3
mainloop()
