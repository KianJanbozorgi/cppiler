import parser_table
import Lexer_cpp

class Parser:
    def __init__(self, parse_table):
        self.parse_table = parse_table

    def walk(self, tokens):
        current_token = 0
        node = 0
        parse_tree = []
        lvl = 0
        stack = ["Start"]

        while stack:
            top_stack = stack.pop() # O(1)
            if top_stack == "$":
                if current_token == len(tokens):
                    return parse_tree

            elif top_stack in self.parse_table:
                token = tokens[current_token][1] if current_token < len(tokens) else "$"
                rule = self.parse_table[top_stack].get(token)

                if not rule:
                    token = tokens[current_token][0]
                    rule = self.parse_table[top_stack].get(token)

                    if not rule:
                        raise ValueError(f"Syntax error: expected '{top_stack}', got '{tokens[current_token][1]}' at line {tokens[current_token][2]}")

                for j in parse_tree: #O(r) where r is the number of rules
                    if top_stack in j[1]:
                        lvl = j[0][1] + 1
                parse_tree.append([(top_stack, lvl), []])

                children = rule.split()
                for child in reversed(children): #O(c) where c is the number of childrens
                    if child != "ε":
                        stack.append(child)

                for child in reversed(children): #O(c) where c is the number of childrens
                    parse_tree[node][1].append(child)
                node += 1

            else:
                token = tokens[current_token][1]
                if token == top_stack:
                    current_token += 1
                elif tokens[current_token][0] == top_stack:
                    parse_tree[node - 1][1].append(tokens[current_token][1]) #O(1)
                    current_token += 1
                else:
                    raise ValueError(f"Syntax error: expected '{top_stack}', got '{token}' at line {tokens[current_token][2]}")

        return parse_tree
    # overall O(n*2c + n*r)
 