from antlr4 import FileStream
from antlr4 import CommonTokenStream
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from TreeVisitor import TreeVisitor
from EvalVisitor import EvalVisitor

input_stream = FileStream("text.txt")
lexer = FunxLexer(input_stream)
token_stream = CommonTokenStream(lexer)
parser = FunxParser(token_stream)
tree = parser.root()
visitor = TreeVisitor()
evaluator = EvalVisitor({})
# visitor.visit(tree)
print('---------------------')

r = evaluator.visit(tree)
print(r)
