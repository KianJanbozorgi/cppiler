import parser_table
import Lexer_cpp

class Parser:
    def __init__(self, parse_table):
        self.parse_table = parse_table
    def walk(self,tokens):
        current_token = 0 # iterating tokens
        node = 0    #iterating tree
        parse_tree = []
        stack = ["Start"]
        while stack:
            top_stack = stack.pop()
            if top_stack == "$": # stack getting empty meaning that PDA is in accept state
                if current_token == len(token):  
                    return parse_tree
            elif top_stack in self.parse_table: # for iterating the variables
                token = tokens[current_token][1] if current_token < len(tokens) else "$" 
                rule = self.parse_table[top_stack].get(token)
                if not rule:
                        token = tokens[current_token][0]
                        rule = self.parse_table[top_stack].get(token)
                        if not rule:
                            print(tokens[current_token])

                            
                parse_tree.append([top_stack , []])
                children = rule.split()
                for child in reversed(children):
                    if child != "ε":
                        stack.append(child) # updating stack and tree
                for child in reversed(children):
                    parse_tree[node][1].append(child)
                node += 1

            else: # getting a terminal or epsilon
                token = tokens[current_token][1]  
                if token == top_stack:  
                    current_token += 1 # moving forward in tokens    
                elif tokens[current_token][0] == top_stack:
                    parse_tree[node-1][1].clear()
                    parse_tree[node-1][1].append(tokens[current_token][1])
                    current_token += 1 # getting identifiers and numbers in tree
        return parse_tree 

tokens_list = Lexer_cpp.tokens_list

parser = Parser(parser_table.parse_table)

parse_tree = parser.walk(tokens_list)
print("\nParse Tree:")

for i in parse_tree:
    print(f"{i[0]} --> {i[1]}")


