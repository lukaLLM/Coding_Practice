class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x==0 or x==1:
            return x
        else:
            # Normal search by multiplyfig give time complexity O(sqrt (n))
            # binary search for time complexity O(log n)
            left = 0
            right = x
            while left <= right:
                mid = (left + right) // 2
                if mid * mid < x: # that mean the number is not on lefy side
                    left = mid + 1
                elif mid * mid > x: # that mean the number is not on right side
                    right = mid - 1 # 
                else:
                    return mid
            return right # return to get the lower integer value

solution = Solution()
print(solution.mySqrt(5) )