"""
https://leetcode.com/problems/palindrome-number/description/

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.



"""


class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        array = str(x)
        length = len(array) - 1
        for n in range(len(array)):
            if n >= length:
                return True    
            if array[n] != array[length]:
                return False
            length = length - 1    