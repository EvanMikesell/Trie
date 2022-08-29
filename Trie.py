class Trie:

    def __init__(self):
        self.root = self.Node('', False)

    def insert(self, word: str):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = self.Node(char, False)

            current_node = current_node.children[char]

        # last letter of the word is the end of the word
        current_node.is_end_of_word = True

    def find_words(self, substring='') -> list:
        return self.root.find_words('', self.root, substring)

    class Node:
        """def __init__(self):
            self.letter = ''
            self.isEndofWord = False
            self.children = dict()"""

        def __init__(self, letter: str, is_end_of_word: bool):
            self.letter = letter
            self.is_end_of_word = is_end_of_word
            self.children = dict()

        def find_words(self, word: str, current_node: 'Node', substring: str = '', word_list: list = []) -> list:
            word += current_node.letter
            if current_node.is_end_of_word:
                if substring in word:
                    word_list.append(word)
            for child in current_node.children.values():
                self.find_words(word, child, substring, word_list)
            return word_list


tree = Trie()
tree.insert('dog')
tree.insert('log')
tree.insert('day')
tree.insert('hello')
tree.insert('hi')

ar_words = tree.find_words(substring='ar')
print("Words with 'ar'", ar_words)

all_words = tree.find_words()
print("All words", all_words)
