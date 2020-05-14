from regex_engine.conversion.tools import NdeaNode


def node_to_ndea_node(base_node):
    """
    Converts a regex grammar tree (of type node) to an NDEA (of type NdeaNode)
    :param base_node: The regex grammar tree
    :return: An NDEA node structure (returns the start node)
    """
    if base_node.is_leaf():
        start_node = NdeaNode()
        end_node = NdeaNode(end_node=True)
        start_node.add_transition(base_node.value, end_node)
        return start_node

    if base_node.value in ["°", "|", "*"]:
        ndea_child_nodes = [node_to_ndea_node(child) for child in base_node.children]
        operation = base_node.value
        if operation == "°":
            for i, ndea_child_node in enumerate(ndea_child_nodes):
                if len(ndea_child_nodes) > i + 1:
                    ndea_child_node.reroute_endnodes(ndea_child_nodes[i + 1])
            ndea_start_node = ndea_child_nodes[0]
            return ndea_start_node

        elif operation == "|":
            ndea_start_node = NdeaNode()
            for child_node in ndea_child_nodes:
                ndea_start_node.add_transition(None, child_node)
            return ndea_start_node

        elif operation == "*":
            ndea_start_node = NdeaNode(end_node=True)
            child_node = ndea_child_nodes[0]
            ndea_start_node.add_transition(None, child_node)
            child_node.reroute_endnodes(ndea_start_node)
            return ndea_start_node
