#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。
class Solution:
    def singleNumber(self, nums) -> int:
        #方法一数学思维，总和误差为只出现一次的数字
        a =set()
        sum1 = 0
        sum2 = 0
        for i in range(len(nums)):
            a.add(nums[i])
            sum1 +=nums[i]
        for i in a:
            sum2 +=i
        #print(sum2*2-sum1)
        return sum2*2-sum1
        #方法二，异或,大神思维
        #a^a=0,a^0=a,异或具备交换律！
        a =nums[0]
        for i in range(1,len(nums)):
            a = a^nums[i]
        print(a)

if __name__=="__main__":
    nums = [4,1,2,1,2]

    x = Solution().singleNumber(nums)