## Lexical analyzer

Write a program, that reads an input and converts it into a sequence of lexical symbols – *tokens*. Each token is a pair, it composes from a type and possibly a value.

The tokens definition depends on you, and it is considered a part of the solution.

### Input specification

The input may be containing the following symbols:

- *identifiers* - consisting of a sequence of letters and numbers starting with a letter
- *numbers* - formed by a sequence of decimal digits
- *operators* - symbols `'+', '-', '*' and '/'`,
- *delimiters* - symbols `'(', ')' and ';'`,
- *keywords* - `div` and `mod`.

Symbols can be separated by a sequence of spaces, tabs, and line breaks.

There can be notes in the input. Notes are preceded by a sequence `//` and continue to the end of the line.

*White spaces and notes does not produce any lexical symbols.*

### Output specification

Converts the given input into a sequence of tokens and write them on output. Write each token on a separated line.

#### Example

##### Input

    -2 + (245 div 3);  // note
    2 mod 3 * hello

##### Output

*Your output can be different, it depends on your definition of tokens.*

    OP:-
    NUM:2
    OP:+
    LPAR
    NUM:245
    DIV
    NUM:3
    RPAR
    SEMICOLON
    NUM:2
    MOD
    NUM:3
    OP:*
    ID:hello