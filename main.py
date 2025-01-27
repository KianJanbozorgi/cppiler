import Lexer_cpp , parser_cpp , parser_table , error_handeling , identifier_finder


cpp_code = """#include
using namespace std;
int main(){
int x;
int s = 0, t=10;
while (t >= 0){
cin>>x;
s = 4; 
}
cout<<"sum="<<s;
return 0;
}
}"""

lex = Lexer_cpp.Lexer(cpp_code)
tokens_list = lex.move_forw()
print(tokens_list)

parse_table = parser_table.parse_table

parser = parser_cpp.Parser(parse_table)

error_handeling.validate_assignments(tokens_list)
error_handeling.validate_semicolons(tokens_list)

parse_tree = parser.walk(tokens_list)
print("Parse tree:")
for node in parse_tree: # O(n) where n is number of nodes in the tree  
    print(f"{node[0]} --> {node[1]}")

identifier = "t"

parse_tree_dict = identifier_finder.parse_tree_dict_maker(parse_tree)


print(identifier_finder.find_first_assignment(parse_tree_dict , identifier))