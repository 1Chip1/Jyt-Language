from lexer import Lexer
from parser import Parser
from evaluator import Evaluator

def main():
    file = open("main.jyt",'r')
    lexer = Lexer(file)
    parser = Parser(lexer.tokens)
    
    lexer.tokenizer()


    parser.build_AST()
 

    evaluator = Evaluator(parser.AST)
    evaluator.run(parser.AST)
  

if __name__ == "__main__":
    main()