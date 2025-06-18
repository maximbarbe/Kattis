class TrieNode:
    
    def __init__(self):
        self.children = [None] * 10
        self.ends = False
        self.n = 0
        
    def add_word(node, word, idx):
        if idx == len(word):
            node.ends = True
            return
        if node.children[ord(word[idx]) - ord("0")] == None:
            node.children[ord(word[idx]) - ord("0")] = TrieNode()
        TrieNode.add_word(node.children[ord(word[idx]) - ord("0")], word, idx + 1)  
    def get_children(node):
        if not node:
            return 0
        else:
            if node.ends:
                num = 1 + sum([TrieNode.get_children(c_node) for c_node in node.children])
                node.n = num
                return num
            else:
                num = sum([TrieNode.get_children(c_node) for c_node in node.children])
                node.n = num
                return num
            
    def get_res(root, word, idx):
        if not root:
            return 0
        elif idx == len(word):
            return root.n
        else:
            return TrieNode.get_res(root.children[ord(word[idx]) - ord("0")], word, idx + 1)
        
root = TrieNode()


n = int(input())
for i in range(n):
    word = input()
    TrieNode.add_word(root, word, 0)
TrieNode.get_children(root)
q = int(input())
for i in range(q):
    print(TrieNode.get_res(root, input(), 0))