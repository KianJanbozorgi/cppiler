# Cppiler - A C++ Compiler

**Cppiler** is a compiler front-end for a subset of C++ syntax, demonstrating lexical analysis, syntax parsing, and semantic error checking. It includes components for tokenization, parse tree generation, and validation of assignments and syntax rules.

## Features

- **Lexical Analysis**: Tokenizes C++ code into identifiers, reserved words, symbols, numbers, and strings.
- **Syntax Parsing**: Uses a parse table and predictive parsing to build a parse tree.
- **Semantic Checks**:
  - Validates variable assignments (e.g., ensuring identifiers are declared before use).
  - Detects missing semicolons.
- **Identifier Tracking**: Traverses the parse tree to find the first assignment of a variable.
- **Error Handling**: Provides descriptive error messages with line numbers.

## Project Structure

| File                | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| `Lexer_cpp.py`      | Tokenizes input C++ code into lexemes.                                      |
| `parser_cpp.py`     | Predictive parser that constructs a parse tree using grammar rules.        |
| `parser_table.py`   | Defines grammar production rules for the parser.                            |
| `error_handling.py` | Validates assignments and checks for missing semicolons.                    |
| `identifier_finder.py` | Traverses the parse tree to resolve variable assignments.               |
| `main.py`           | Demonstrates the compilation pipeline with example code.                   |
| `tokenTable.py`     | Generates a categorized summary of tokens.                                 |

## Usage

### Prerequisites
- Python 3.x

### Running the Project
1. Clone the repository.
2. Run the `main.py` script:
   ```bash
   python main.py
