import parser_table
import Lexer_cpp

class Parser:
    def __init__(self, parse_table):
        self.parse_table = parse_table
    def walk(self,tokens):
        current_token = 0 # iterating tokens
        node = 0    #iterating tree
        parse_tree = []
        lvl = 0
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
                            for i in parse_tree:
                                print(f"{i[0]} --> {i[1]}")
                            print(stack)
                            raise ValueError(f"Syntax error: expected '{top_stack}', got '{tokens[current_token][1]}")
                for j in parse_tree:
                    if top_stack in j[1]:
                        lvl = j[0][1] + 1  # added property level to be more tree-like          
                parse_tree.append([(top_stack , lvl)  , []])
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
                    parse_tree[node-1][1].append(tokens[current_token][1])
                    current_token += 1 # getting identifiers and numbers in tree
                    j = 1
                else:
                    for i in parse_tree:
                        print(f"{i[0]} --> {i[1]}")
                    print(stack)
                    raise ValueError(f"Syntax error: expected '{top_stack}', got '{token}'")
        return parse_tree 

tokens_list = Lexer_cpp.tokens_list

parser = Parser(parser_table.parse_table)

parse_tree = parser.walk(tokens_list)
parse_tree_dict = {}
for i in parse_tree:
    parse_tree_dict[i[0]] = i[1] # saving the parse tree in some kind of a hash table(dictionary)
print(parse_tree_dict)
print("\nParse Tree:")

for i in parse_tree:
    print(f"{i[0]} --> {i[1]}")


def find_first_assignment(parse_tree_dict, identifier):
    stack = [("Start" , 0)]  # Start DFS with the root node
    ids = []
    assigns = []
    operations = []
    value = 0 
    while stack:
        current_node = stack.pop()
        label, level = current_node
        try:
            children = parse_tree_dict[current_node] # skiping leaves
        except:
            continue
        if  label == "Id":
            ids.append(children)
        if identifier in children:
            if "Assign" in children:
                assigns.append(parse_tree_dict[("Assign" , level+1)]) # checkin if the identifier is assigned to a value
                try:
                    operations.append(parse_tree_dict[("Operation" , level+2)]) # checking the value of assignment
                except:
                    break
                break        
            else:
                break
        else:
            for child in children:
                stack.append((child , level+1)) # iterating leftmost cgildrens firs as DFS 
    id_ide = ids[-1][1]
    if "=" in assigns[0]:
        as_ide = "="
        num_ide= operations[0][-1]
    else:
        as_ide = ""
        num_ide = ""
    value = id_ide + " " + identifier + " " + as_ide + " " + num_ide          
    return value
print(find_first_assignment(parse_tree_dict , "s"))