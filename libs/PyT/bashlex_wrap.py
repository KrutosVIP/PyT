# Bash-lex wrapper.
import bashlex

i = "sudo rm -rf /* > log.txt && cat log.txt || export a='mom' && echo $(pwd):$a"
def _parser(text):
    parse_ = bashlex.parse(text)
    for i2 in parse_:
        print(" ")
        print(i2.dump())

_parser(i)
