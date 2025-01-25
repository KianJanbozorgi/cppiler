import Lexer_cpp

t = Lexer_cpp.tokens_list
token_table = {
    "string":[],
    "number":[],
    "symbol":[],
    "identifier":[],
    "reserved_word":[]
}
for token in t:
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
for token in token_table:
    token_table[token] = sorted(token_table[token])
print(token_table)