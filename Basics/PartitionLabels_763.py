# Status: Bad

class Solution:
    def findLastIndex(self, s, x):
            index = -1
            for i in range(0, len(s)):
                if s[i] == x:
                    index = i
            return index

    def partitionLabels(self, s: str) -> list[int]:  
        answ = []
        begin = 0
        while s:
            idx = self.findLastIndex(s, s[begin])
            unique = set(s[begin:idx+1])
           
            for i in range(len(unique)):
                subidx = self.findLastIndex(s, list(unique)[i])
                unique = set.union(unique, set(s[begin:subidx+1]))
                for j in unique:
                    subidx = self.findLastIndex(s, j)
                    unique = set.union(unique, set(s[begin:subidx+1]))
            
            temp = []
            for char in unique:
                temp.append(self.findLastIndex(s, char))

            partition = max(temp)
            if idx < partition:
                answ.append(partition+1)
                s = s[partition+1:]
            else:
                answ.append(idx+1)
                s = s[idx+1:]
        return answ          

solve = Solution()
print(solve.partitionLabels("qiejxqfnqceocmy")) # [13,1,1]
print(solve.partitionLabels("mlullbhiuiujgvwvurcdvhzdk")) # [1,23,1]
print(solve.partitionLabels("ababcbacadefegdehijhklij")) # [9,7,8]
