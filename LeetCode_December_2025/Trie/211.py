from string import ascii_lowercase 

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur_node = self.root 
        for char in word:
            if char not in cur_node.children:
                cur_node.children[char] = TrieNode()
            cur_node = cur_node.children[char]

        cur_node.word = True        

    def simple_search(self, word):
        cur_node = self.root
        for char in word:
            if char not in cur_node.children:
                return False
            cur_node = cur_node.children[char]
        
        return cur_node.word

    def search(self, word: str) -> bool:
        i = 0 
        while i < len(word) and word[i] != '.':
            i += 1
        
        if i == len(word): 
            return self.simple_search(word)
        
        # found dot
        prefix = ""
        cur_node = self.root
        for j in range(i):
            if word[j] not in cur_node.children:
                return False
            prefix += word[j]
            cur_node = cur_node.children[word[j]]
        
        nodes, words = [], []
        for char in cur_node.children.keys():
            words.append(prefix+char)
            nodes.append(cur_node.children[char])
        
        i = i+1
        while i < len(word) and word[i] != '.':
            for idx in range(len(words)):
                if nodes[idx]:
                    if word[i] in nodes[idx].children:
                        nodes[idx] = nodes[idx].children[word[i]]
                        words[idx] = words[idx] + word[i]
                    else:
                        nodes[idx], words[idx] = None, None
            i += 1
        
        if i == len(word):
            for w in words:
                if w:
                    if self.simple_search(w):
                        return True
            return False
        
        # found second dot
        words_ii = []
        for idx in range(len(words)):
            if nodes[idx]:
                for char in nodes[idx].children.keys():
                    words_ii.append(words[idx]+char)

        i += 1
        while i < len(word):
            for idx in range(len(words_ii)):
                words_ii[idx] = words_ii[idx] + word[i]
            i += 1

        for w in words_ii:
            if self.simple_search(w):
                return True
        
        return False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

def test(op, input):
    obj = eval(f"{op[0]}()")
    for i in range(1, len(input)):
        # if not input[i]:
        #     print(eval(f"obj.{op[i]}()"))
        print(eval(f"obj.{op[i]}('{input[i][0]}')"))

op = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
inp = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]

# test(op, inp)

import random as r

def test_algo():
    obj = WordDictionary()
    op = ["WordDictionary"]
    inp = [[]]
    
    add_number = r.randrange(5, 10)
    words = []
    for _ in range(add_number):
        length = r.randrange(1, 25)
        w = "".join(r.choice(ascii_lowercase) for _ in range(length))
        op.append("addWord")
        inp.append([w])
        words.append(w)
        obj.addWord(w)
    
    # print(wordcs)
    for _ in range(len(words)):
        yes_or_no = r.choice([True, False])
        if yes_or_no:
            w = r.choice(words)
        else:
            w = "".join(r.choice(ascii_lowercase) for _ in range(length))

        if w in words:
            continue
        dot1 = r.choice([True, False])
        idx = None
        if dot1:
            idx = r.choice(range(0, len(w)))
            # w[idx] = '.'
            w = w[:idx] + '.' + w[idx+1:]
        dot2 = r.choice([True, False])
        if dot2:
            idx2 = r.choice(range(0, len(w)))
            # while idx2 == idx: idx2 = r.choice(range(0, len(w)))
            w = w[:idx2] + '.' + w[idx2+1:]
        op.append("search")
        inp.append([w])
        # print(w)
        val = obj.search(w)
        # if val == True:
        #     return (True, words, w)
    print("---------------")
    print(f"{op}".replace('\'', '\"'))
    print(f"{inp}".replace('\'', '\"'))
    return (False, words, w)
        
test_algo()

for i in range(10):
    res, words, sword = test_algo()
    
    if res:
        print(words)
        print(sword)
        # break

        # found second dot
        # for j in range(ii, i):
        #     for idx in range(len(words)):
        #         nodes[idx] = nodes[idx].children[word[j]]
        #         words[idx] = words[idx] + word[j]