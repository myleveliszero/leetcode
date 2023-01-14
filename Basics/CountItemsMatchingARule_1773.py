# Status: Good

class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        answ = 0
        if ruleKey is "type":
            idx = 0
        elif ruleKey is "color":
            idx = 1
        else:
            idx = 2            

        for i in items:
            if i[idx] is ruleValue:
                answ += 1
        return answ
           


solve = Solution()
print(solve.countMatches(items = [["phone","blue","pixel"],
["computer","silver","lenovo"],["phone","gold","iphone"]],
 ruleKey = "color", ruleValue = "silver"))
print(solve.countMatches(items = [["phone","blue","pixel"],["computer","silver","phone"],
["phone","gold","iphone"]], ruleKey = "type", ruleValue = "phone"))