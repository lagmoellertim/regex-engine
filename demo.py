from regex_engine import RegexEngine

engine = RegexEngine("a|(b(ac)*12+3)")

print(engine.check_word("a"))  # True
print(engine.check_word("aa"))  # False
print(engine.check_word("b123"))  # True
print(engine.check_word("bac1222223"))  # True
print(engine.check_word("ba1222223"))  # False
print(engine.check_word("bacac122222"))  # False
