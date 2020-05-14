class Node:
    def __init__(self, value):
        """
        Initializes a node with a value
        :param value: The value of the node
        """
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, node):
        """
        Adds a child node to this node (the new parent of the child)
        :param node: The new child node
        :return:
        """
        self.children.append(node)
        node.parent = self

    def is_leaf(self):
        """
        Checks whether the node has children or not
        :return: True if leaf, else False
        """
        return len(self.children) == 0

    def __pretty_print(self, indent=0):
        """
        Pretty output of the Node Object
        :param indent:
        :return:
        """
        output = [" " * indent + "-" + self.value]
        for child in self.children:
            output.append(child.__pretty_print(indent + 1))
        return "\n".join(output)

    def __repr__(self):
        return self.__pretty_print()
