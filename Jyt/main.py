from lexer import Lexer
from parser import Parser
from evaluator import Evaluator

def main():
    filename = "debug.jyt"
    file = open(filename, 'r')
    lexer = Lexer(file)
    parser = Parser(lexer.tokens)

    evaluator = Evaluator(parser.AST)

    evaluator.run(parser.AST)
    

if __name__ == "__name__":
    main()