from regex_engine.conversion.tools import Node


def regex_to_node(regex):
    """
    Converts a regular expression to a tree node (recursive)
    :param regex: The regular expression (grammar)
    :return: The root node, containing the regex grammar tree
    """
    regex_parts = []

    current_bracket = 0
    current_string = ""

    for char in regex:
        if char == "(":
            if current_bracket > 0:
                current_string += char
            current_bracket += 1

        elif char == ")":
            current_bracket -= 1

            if current_bracket > 0:
                current_string += char
            else:
                regex_parts.append(current_string)
                current_string = ""

        else:
            if current_bracket == 0:
                regex_parts.append(char)
            else:
                current_string += char

    if current_bracket != 0:
        raise Exception("Syntax Error: Bracket Pairs don't match up")

    if "|" in regex_parts:
        regex_parts_with_new_brackets = []
        for char in regex_parts:
            if char not in ["*", "+", "|"]:
                regex_parts_with_new_brackets.append(f"({char})")
            else:
                regex_parts_with_new_brackets.append(char)

        operator_position = regex_parts_with_new_brackets.index("|")

        left_regex_part = regex_parts_with_new_brackets[:operator_position]
        right_regex_part = regex_parts_with_new_brackets[operator_position + 1:]

        left_sub_node = regex_to_node("".join(left_regex_part))
        right_sub_node = regex_to_node("".join(right_regex_part))

        alternative_node = Node("|")
        alternative_node.add_child(left_sub_node)
        alternative_node.add_child(right_sub_node)

        return alternative_node

    nodes_to_join = []
    for pos, regex_part in enumerate(regex_parts):
        if regex_part not in ["*", "+", "|"]:
            if len(regex_parts) > pos + 1 and regex_parts[pos + 1] in ["*", "+"]:
                if regex_parts[pos + 1] == "*":
                    repeat_node = Node("*")
                    repeat_node.add_child(regex_to_node(regex_part))
                    nodes_to_join.append(repeat_node)

                elif regex_parts[pos + 1] == "+":
                    repeat_min_once_node = regex_to_node(f"(({regex_part})*({regex_part}))")
                    nodes_to_join.append(repeat_min_once_node)
            else:
                if len(regex_part) != 1:
                    regex_node = regex_to_node(regex_part)
                    nodes_to_join.append(regex_node)
                else:
                    leaf_node = Node(regex_part)
                    nodes_to_join.append(leaf_node)

    if len(nodes_to_join) == 1:
        return nodes_to_join[0]

    joined_node = Node("°")

    for node in nodes_to_join:
        joined_node.add_child(node)

    return joined_node
