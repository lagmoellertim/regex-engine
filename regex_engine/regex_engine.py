from regex_engine.conversion import regex_to_node, node_to_ndea_node


class RegexEngine:
    def __init__(self, regex):
        """
        Creates a RegexEngine instance with a regex grammar
        :param regex: The grammar to use
        """

        self.node = regex_to_node(regex)
        self.ndea_node = node_to_ndea_node(self.node)

    def check_word(self, word):
        """
        Checks whether a word is included in the grammar
        :param word: The word to be tested
        :return: If it is a part of the grammar
        """
        return self.ndea_node.check_word(word)
