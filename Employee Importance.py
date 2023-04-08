# Time Complexity : O(n)
# Space Complexity : O(n)
# Did this code successfully run on Leetcode : yes
# Any problem you faced while coding this : no


"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        q = []
        hashmap = {}
        value = {}
        for e in employees:
            hashmap[e.id] = e.subordinates
            value[e.id] = e.importance
        result = value[id]
        q.extend(hashmap[id])
        while(len(q)> 0 ):
            emp = q.pop(0)
            result += value[emp]
            q.extend(hashmap[emp])
        return result