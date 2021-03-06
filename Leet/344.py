class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        right = len(s) -1
        left = 0
        
        while left < right:
            s[left],s[right] = s[right],s[left]
            left +=1
            right -= 1
        return s