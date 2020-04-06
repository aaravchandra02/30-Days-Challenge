"""
Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Group_Anagrams:
    def groupAnagrams(self, strs):
        """
        Basic Idea:
        Iterate over elements and sort each alphabetically. we will make them as keys.
        Same keys for anagram 
        """
        d = {}
        for i in strs:
            tmp = sorted(i)
            tmp = "".join(tmp)
            d.setdefault(tmp, [])
            d[tmp].append(i)
        print(d.values())


a = Group_Anagrams()
a.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
