"""Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?"""

from collections import deque
from queue import LifoQueue


class Solution:
    def backspaceCompare_list(self, S: str, T: str) -> bool:
        s = []
        t = []
        for i in S:
            if(i == '#'):
                if(len(s) < 1):
                    continue
                s.pop()
            else:
                s.append(i)

        for i in T:
            if(i == '#'):
                if(len(t) < 1):
                    continue
                t.pop()
            else:
                t.append(i)

        return(s == t)

    def backspaceCompare_deque(self, S: str, T: str) -> bool:
        s = deque()
        t = deque()
        for i in S:
            if(i == '#'):
                if(len(s) < 1):
                    continue
                s.pop()
            else:
                s.append(i)

        for i in T:
            if(i == '#'):
                if(len(t) < 1):
                    continue
                t.pop()
            else:
                t.append(i)

        return(s == t)
