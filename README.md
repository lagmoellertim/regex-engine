# RegexEngine

A small regex engine that parses strings to a syntax tree and validates words using an NDEA


## Operations

- a | b means a or b (Alternative)
- ab means a and b (Joined)
- a* means nothing or as many a's you want (Repetition or Nothing)
- a+ means one or as many a's you want (Repetition)
- (a|b) works exactly like brackets in any other context
    - (ab)* = abababab...
    - (ab)(ab) = abab
    - (ab)|(c*) = ab | ccccc....
    - (a|(b|(c|(d)))) = a|b|c|d

## How to use it
Works with any Python version >3.5

You can find some usage demos in the demo.py

Have fun!
