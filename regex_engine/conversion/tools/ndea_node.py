class NdeaNode:
    def __init__(self, end_node=False):
        """
        Initializes an NdeaNode, which by default is not an end node
        :param end_node: Whether the node should be an end node
        """
        self.transitions = {}
        self.endnode = end_node

    def add_transition(self, letter, node):
        """
        Adds a transition to the current node to get to another node
        :param letter: A symbol or None (for always transition)
        :param node: The node to arrive at
        :return:
        """
        if letter not in self.transitions.keys():
            self.transitions[letter] = []

        if node not in self.transitions[letter]:
            self.transitions[letter].append(node)

    def reroute_endnodes(self, new_endnode, already_traversed=None):
        """
        Remove all endnodes associated with this node and reroute them to the new endnode
        :param new_endnode: The new endnode
        :param already_traversed: Contains all nodes that have already been checked to avoid loops
        :return:
        """
        if already_traversed is None:
            already_traversed = []

        if self not in already_traversed:
            if self.endnode:
                self.endnode = False
                self.add_transition(None, new_endnode)

            else:
                already_traversed = already_traversed[::]
                already_traversed.append(self)

                for _, transition_node_list in self.transitions.items():
                    for transition_node in transition_node_list:
                        transition_node.reroute_endnodes(new_endnode, already_traversed)

    def check_word(self, word):
        """
        Checks whether a word is contained in the NDEA or not
        :param word: The word to check
        :return: Whether the word is included
        """
        if len(word) > 0:
            letter = word[0]

            if letter in self.transitions.keys():
                for transition in self.transitions[letter]:
                    if transition.check_word(word[1:]):
                        return True

            if None in self.transitions.keys():
                for transition in self.transitions[None]:
                    if transition.check_word(word):
                        return True

            return False

        else:
            if self.endnode:
                return True

            if None in self.transitions.keys():
                for transition in self.transitions[None]:
                    if transition.endnode:
                        return True

            return False

    def __pretty_print(self, indent=0, traversed_items=None):
        """
        Pretty output of the NDEA Tree Node structure
        :param indent:
        :param traversed_items:
        :return:
        """
        if traversed_items is None:
            traversed_items = []

        if self in traversed_items:
            return f"{indent * ' '} Loop detected"

        traversed_items.append(self)
        output = []

        for letter, transition_node_list in self.transitions.items():
            if letter is None:
                letter = "ε"

            endnode_text = ": Endnode" if self.endnode else ""

            output.append(f"{indent * ' '}-{letter}{endnode_text}")

            for transition_node in transition_node_list:
                output.append(transition_node.__pretty_print(indent + 1, traversed_items))

        return "\n".join(output)

    def __repr__(self):
        return self.__pretty_print()
