#题目 编写一个函数，输入n为偶数时，调用函数求1/2+1/4+…+1/n,当输入n为奇数时，调用函数1/1+1/3+…+1/n
def even(n):
    sum = 0.0
    for i in range(2,n+1,2):
        sum +=1.0/i
    return sum

def odd(n):
    sum = 0.0
    for i in range(1, n+1, 2):
        sum +=1.0/i
    return sum

if __name__=="__main__":
    print("请输入一个num:",end="")
    num = int(input())
    if num%2==0:
        sum = even(num)
    else:
        sum = odd(num)

    print(sum)
