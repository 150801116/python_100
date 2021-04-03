#题目 文本颜色设置。
#很明显这触及了我的知识盲区了！参考答案看了 也很麻木。。。。
#参考答案
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
print(bcolors.HEADER + "警告的颜色字体?" + bcolors.OKGREEN)