import re
Let = 'letter'
Ide = 'identifier'
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

    def move_forw(self): #O(n) where n is the number of characters
        tokens = []
        current = 0
        l_number = 0
        while current < len(self.text):
            char = self.text[current]
            if char == '\n':
                l_number += 1
            # Skip whitespace
            if re.match(whitespace, char):
                current += 1
                continue

            # Handle symbols
            if char in symbols:
                if current + 1 < len(self.text) and self.text[current:current + 2] in symbols:
                    tokens.append([Sym, self.text[current:current + 2] , l_number])
                    current += 2
                    continue
                tokens.append([Sym, char , l_number])
                current += 1
                continue

            # Handle numbers
            if re.match(digits, char):
                s = ''
                while current < len(self.text) and re.match(digits, self.text[current]):
                    s += self.text[current]
                    current += 1
                
                tokens.append([Nu, s , l_number])
                continue

            # Handle identifiers and reserved words
            if re.match(letters, char):
                s = ''
                while current < len(self.text) and (re.match(letters, self.text[current]) or re.match(digits, self.text[current])):
                    s += self.text[current]
                    current += 1
                if s in reserved_words:
                    tokens.append([Res, s , l_number])
                else:
                    tokens.append([Ide,s , l_number ])
                continue

            # Handle strings
            if char == '"':
                s = ''
                current += 1
                while current < len(self.text) and self.text[current] != '"':
                    s += self.text[current]
                    current += 1
                tokens.append([St, s , l_number])
                current += 1  # Move past the closing quote
                continue

            # Increment for unrecognized characters
            current += 1

        return tokens




