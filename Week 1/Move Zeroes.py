"""
Move Zeroes

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.

        Do not return anything, modify nums in-place instead.
    
"""


class Move_Zeroes:
    def moveZeroes_extra_space(self, nums):
        """
        Basic idea : 
        Store all non-zero elements in a separate list and then count the occurences of zeros.
        Next, append the numbers of zeros in the new list and return it.
        """
        c = 0
        l = []
        for i in nums:
            if(i == 0):
                c += 1
            else:
                l.append(i)
        for i in range(c):
            l.append(0)
        print(l)

    def moveZeroes_no_extra_space_1(self, a):
        """
        Basic idea : 
        One as start (points at 0) and the other as last (points at the end)
        Looping through every element, start+=1 if non- zero element is met.
        As soon as a zero is encountered-> keep swapping with the immediate right element until last position is met.
        reduce last by 1 and set start=0 to make sure no zeros were swapped like in [0,0,1]
        """
        last = len(a)-1
        start = 0
        while(start < last):
            if a[start] == 0:
                for j in range(start, last):
                    a[j], a[j+1] = a[j+1], a[j]
                    if (j+1 == last):
                        last -= 1
                        start = 0
            else:
                start += 1

        print(a)

    def moveZeroes_no_extra_space_2(self, nums):
        """
        Basic Idea:
        Overwrite non-zero elements in the array and keep count of over-written elements
        In the other loop, from the current count to the length of the original array, append as many zeros.
        """
        i = 0
        for n in nums:
            if n != 0:
                nums[i] = n
                i += 1

        while i < len(nums):
            nums[i] = 0
            i += 1


a = Move_Zeroes()
a.moveZeroes_no_extra_space([0, 1, 0, 3, 12])
