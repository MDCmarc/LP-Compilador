# Generated from Funx.g4 by ANTLR 4.7.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
else:
    from FunxParser import FunxParser

# This class defines a complete generic visitor for a parse tree produced by FunxParser.

class FunxVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by FunxParser#root.
    def visitRoot(self, ctx:FunxParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#function.
    def visitFunction(self, ctx:FunxParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#parameters.
    def visitParameters(self, ctx:FunxParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#instruction.
    def visitInstruction(self, ctx:FunxParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#IfElse.
    def visitIfElse(self, ctx:FunxParser.IfElseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#If.
    def visitIf(self, ctx:FunxParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#loop.
    def visitLoop(self, ctx:FunxParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Equal.
    def visitEqual(self, ctx:FunxParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#NotEqual.
    def visitNotEqual(self, ctx:FunxParser.NotEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Greater.
    def visitGreater(self, ctx:FunxParser.GreaterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Less.
    def visitLess(self, ctx:FunxParser.LessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#GreaterEqual.
    def visitGreaterEqual(self, ctx:FunxParser.GreaterEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#LessEqual.
    def visitLessEqual(self, ctx:FunxParser.LessEqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#assignation.
    def visitAssignation(self, ctx:FunxParser.AssignationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Multiplication.
    def visitMultiplication(self, ctx:FunxParser.MultiplicationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Variable.
    def visitVariable(self, ctx:FunxParser.VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Parentesis.
    def visitParentesis(self, ctx:FunxParser.ParentesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Modulus.
    def visitModulus(self, ctx:FunxParser.ModulusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Division.
    def visitDivision(self, ctx:FunxParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#CallFunction.
    def visitCallFunction(self, ctx:FunxParser.CallFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Plus.
    def visitPlus(self, ctx:FunxParser.PlusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Valor.
    def visitValor(self, ctx:FunxParser.ValorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Power.
    def visitPower(self, ctx:FunxParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by FunxParser#Minus.
    def visitMinus(self, ctx:FunxParser.MinusContext):
        return self.visitChildren(ctx)



del FunxParser