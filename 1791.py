## (1791) find the center of a star graph 
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        if edges[0][0] in edges[1]:
            return edges[0][0] #it will be either this or 0,1
        return edges[0][1]
#leetcode
#opening up this repo to hacktoberfest 2023
