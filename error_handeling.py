import Lexer_cpp
def validate_assignments(tokens): 
        for i in range(len(tokens)): # O(n) where n is the number of tokens 
            if tokens[i][0] == "identifier":
                print("hello")
                if tokens[i-1][1] == "int" or tokens[i-1][1] == "float":
                    print("na hello")
                    if tokens[i+1][1] == "=":
                        if tokens[i+2][0] == "number":
                            continue
                        elif tokens[i+2][0] == "identifier":
                            for j in tokens[:i]: # O(n) where n is the number of left handed tokens
                                if j[1] == tokens[i+2][1]:
                                    print(tokens[i])
                                    continue
                                else:
                                    raise ValueError(f"Invalid assignment '{tokens[i][1]}' at line {tokens[i+2][2]}")
                        else:
                            raise ValueError(f"Invalid assignment '{tokens[i][1]}' at line {tokens[i+2][2]}")
    # over all the time complexity for worst cas is O(n^2) which is not always the case 
def validate_semicolons(tokens): # O(t) where t is the number of tokens
        for i in range(len(tokens)):
            if tokens[i][0] == "identifier" or tokens[i][0] == "number":
                if tokens[i+1][0] == "reservedword" or tokens[i+1][1] == "identifier" :
                    raise ValueError(f"Missing semicolon after '{tokens[i][1]}' at line {tokens[i][2]}") 
                else:
                    continue

tokens = Lexer_cpp.tokens_list