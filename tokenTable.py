import Lexer_cpp

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

lexer = Lexer_cpp.Lexer(cpp_code)
t = lexer.move_forw()
token_table = { # modifiying the hashes 
    "string":[],
    "number":[],
    "symbol":[],
    "identifier":[],
    "reserved_word":[]
}
for token in t: # modifying the values and putting them in a sorted array(chaining) // O(t) where t is the  number of tokens
    if token[0] == Lexer_cpp.St:
        token_table["string"].append(token[1])
    elif token[0] == Lexer_cpp.Nu:
        token_table["number"].append(token[1])
    elif token[0] == Lexer_cpp.Sym:
        token_table["symbol"].append(token[1])
    elif token[0] == Lexer_cpp.Ide:
        token_table["identifier"].append(token[1])
    elif token[0] == Lexer_cpp.Res:
        token_table["reserved_word"].append(token[1])
for token in token_table: # O(m) where m is the number of types
    token_table[token] = sorted(token_table[token]) #O(n*lg(n))
print(token_table)
# overall O(t + m*n*lg(n))