# 208. Implement Trie (Prefix Tree)
# Medium
#
# 5720
#
# 82
#
# Add to List
#
# Share
# A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.
#
# Implement the Trie class:
#
# Trie() Initializes the trie object.
# void insert(String word) Inserts the string word into the trie.
# boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
# boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#
#
# Example 1:
#
# Input
# ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
# [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
# Output
# [null, null, true, false, true, null, true]
#
# Explanation
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // return True
# trie.search("app");     // return False
# trie.startsWith("app"); // return True
# trie.insert("app");
# trie.search("app");     // return True
#
#
# Constraints:
#
# 1 <= word.length, prefix.length <= 2000
# word and prefix consist only of lowercase English letters.
# At most 3 * 104 calls in total will be made to insert, search, and startsWith.
# Accepted
# 486,183
# Submissions
# 875,022


# %% using Trie Node structure, o(m) for all methods with key/word/prefix with length m

class TrieNode:
    def __init__(self):
        # self.char = char
        self.children = dict()  # key is character, value is TrieNode
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                newNode = TrieNode()
                node.children[char] = newNode
                node = newNode
        # reach end of current word
        node.is_end = True
        return

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char in node.children:
                node = node.children[char]
                continue
            else:
                return False
        # reach end of current word and not returning False
        return node.is_end  # true if exists an exact match

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char in node.children:
                node = node.children[char]
                continue
            else:
                return False
        # reach end of current prefix and not returning False
        return True


# %%
# Your Trie object will be instantiated and called as such:
obj = Trie()
word = 'apple'
obj.insert(word)
print(obj.search('apple'))
print(obj.search('appl'))
print(obj.startsWith('app'))
print(obj.startsWith('appa'))

# %%
# a = 'abc'
# a[:3]
# a[:5] == 'abc'
