"""
Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

Example: 

Input: 19
Output: true

Explanation: 
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
"""


class HappyNumber:
    def check(self, n):
        prev_sums = set()
        while(1):
            if(n == 1):
                return True
            else:
                s, a = 0, 0
                while(n != 0):
                    a = n % 10
                    s += a**2
                    n = n//10
                if (s in prev_sums):
                    return False
                prev_sums.add(s)
                n = s


trying = HappyNumber()
print(trying.check(19))
