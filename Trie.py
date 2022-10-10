class Trie:

    def __init__(self):
        self._root = self.Node('')

    def update(self, word: str):
        """Each letter in a word becomes a child of the previous letter."""
        current_node = self._root
        for letter in word:
            if letter not in current_node._children:
                current_node._children[letter] = self.Node(letter)
            current_node = current_node._children[letter]
        current_node._is_end_of_word = True

    def words(self, substring: str = None) -> list:
        """
        Gets a list of all words in the trie.
        If a substring is specified, it will only include words with the substring.
        """
        all_words = self._root._find_all_words(self._root)
        if not substring:
            return all_words
        else:
            words_containing_substring = []
            for word in all_words:
                if substring in word:
                    words_containing_substring.append(word)
            return words_containing_substring

    def contains(self, word: str) -> bool:
        all_words = self._root._find_all_words(self._root)
        if word in all_words:
            return True
        else:
            return False

    class Node:

        def __init__(self, letter: str):
            self._letter = letter
            self._is_end_of_word = False
            self._children = dict()

        def _find_all_words(self, current_node: 'Node', words: list = None,
                            current_word: str = '') -> list:
            """
            Moves through the tree building up words based on each node's letter.
            Returns a list of all words present in the trie.
            """
            if words is None:
                words = []
            current_word += current_node._letter
            if current_node._is_end_of_word:
                words.append(current_word)
            if current_node._children:
                for child in current_node._children.values():
                    self._find_all_words(child, words, current_word)
            return words
