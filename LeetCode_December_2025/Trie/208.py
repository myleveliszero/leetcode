class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur_node = self.root 
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]
        
        cur_node.word = True    
        

    def search(self, word: str) -> bool:
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        
        return cur_node.word
        

    def startsWith(self, prefix: str) -> bool:
        cur_node = self.root
        for char in prefix:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
       
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def test(op, input):
    obj = eval(f"{op[0]}()")
    for i in range(1, len(input)):
        # if not input[i]:
        #     print(eval(f"obj.{op[i]}()"))
        print(eval(f"obj.{op[i]}('{input[i][0]}')"))

op = ["Trie","insert","search","search","search","startsWith","startsWith","startsWith"]
inp = [[],["hello"],["hell"],["helloa"],["hello"],["hell"],["helloa"],["hello"]]

test(op, inp)