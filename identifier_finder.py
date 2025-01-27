import parser_cpp

parse_tree = parser_cpp.parse_tree

parse_tree_dict = {}
for i in parse_tree: # O(n) which n is number of nodes because the dictionary insertion like hash table is O(1)
    parse_tree_dict[i[0]] = i[1]
    
def find_first_assignment(parse_tree_dict, identifier):
    stack = [("Start" , 0)]  # Start DFS with the root node
    ids = []
    assigns = []
    operations = []
    value = 0 
    while stack: # O(n) where n is the number of nodes in the tree
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
            for child in children: # O(c) where c is the number of childrens
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