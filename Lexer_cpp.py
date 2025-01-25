import re
Let = 'letter'
Ide = 'Identifier'
Dig = 'digit'
Nu = 'number'
Res = 'reservedword'
Sym = 'symbol'
St = 'string'

whitespace = re.compile(r'\s')
reserved_words = [
    'int', 'float', 'void', 'return', 'if', 'while', 'cin', 'cout', 'continue', 'break',
    '#include', 'using', 'iostream', 'namespace', 'std', 'main'
]
digits = re.compile(r'[0-9]')
letters = re.compile(r'[a-zA-Z#]')  
symbols = [
    '(', ')', '|', '[', ']', ',', ';', '+', '-', '*', '/', '==', '!=', '>', '>=', '<', '<=',
    '=', '||', '<<', '>>' , '{' , '}'
]


class Lexer:
    def __init__(self, text):
        self.text = text

    def move_forw(self):
        tokens = []
        current = 0
        while current < len(self.text):
            char = self.text[current]

            # Skip whitespace
            if re.match(whitespace, char):
                current += 1
                continue

            # Handle symbols
            if char in symbols:
                if current + 1 < len(self.text) and self.text[current:current + 2] in symbols:
                    tokens.append([Sym, self.text[current:current + 2]])
                    current += 2
                    continue
                tokens.append([Sym, char])
                current += 1
                continue

            # Handle numbers
            if re.match(digits, char):
                s = ''
                while current < len(self.text) and re.match(digits, self.text[current]):
                    s += self.text[current]
                    current += 1
                
                tokens.append([Nu, s])
                continue

            # Handle identifiers and reserved words
            if re.match(letters, char):
                s = ''
                while current < len(self.text) and (re.match(letters, self.text[current]) or re.match(digits, self.text[current])):
                    s += self.text[current]
                    current += 1
                if s in reserved_words:
                    tokens.append([Res, s])
                else:
                    tokens.append([Ide,s])
                continue

            # Handle strings
            if char == '"':
                s = ''
                current += 1
                while current < len(self.text) and self.text[current] != '"':
                    s += self.text[current]
                    current += 1
                tokens.append([St, s])
                current += 1  # Move past the closing quote
                continue

            # Increment for unrecognized characters
            current += 1

        return tokens


cpp_code = """#include <iostream>
using namespace std;
int main(){
int x;
int s=0, t=10;
while (t >= 0){
cin>>x;
t = t - 1;
s = s + x;
}
cout<<"sum="<<s;
return 0;
}"""

l = Lexer(cpp_code)
print(l.move_forw())
tokens_list = l.move_forw()