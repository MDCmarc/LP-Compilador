if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor


class TreeVisitor(FunxVisitor):
    def __init__(self):
        self.nivell = 0

# ---------------------------------------------------------------
    def visitFuncion(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'Function ' + l[0].getText()+':')
        self.nivell += 1

        print('  ' * self.nivell + 'PARAMS:')
        self.visit(l[2])

        print('  ' * self.nivell + '------------------------------')
        self.nivell += 1
        self.visit(l[4])

        self.nivell -= 1
        self.nivell -= 1
        print('\n')

# ---------------------------------------------------------------
    def visitExprF(self, ctx):
        l = list(ctx.getChildren())
        self.nivell += 1
        print('  ' * self.nivell + 'ExprFinal:')
        self.visit(l[0])
        self.nivell -= 1
# ---------------------------------------------------------------

    def visitParamsFunction(self, ctx):
        l = list(ctx.getChildren())
        for i in range(0, len(l), 2):
            print('  ' * self.nivell + '--> VAR(' + l[i].getText()+')')

# ---------------------------------------------------------------
    def visitVoidFunction(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'NONE')

# ---------------------------------------------------------------
    def visitIf(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'IF')
        self.nivell += 1
        self.visit(l[1])
        self.nivell -= 1

        print('  ' * self.nivell + 'THEN')
        self.nivell += 1
        self.visit(l[3])
        self.nivell -= 1

        print('  ' * self.nivell + 'ENDIF\n')

    def visitIfElse(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'IF')
        self.nivell += 1
        self.visit(l[1])
        self.nivell -= 1

        print('  ' * self.nivell + 'THEN')
        self.nivell += 1
        self.visit(l[3])
        self.nivell -= 1

        print('  ' * self.nivell + 'ELSE')
        self.nivell += 1
        self.visit(l[7])
        self.nivell -= 1

        print('  ' * self.nivell + 'ENDIF\n')


# ---------------------------------------------------------------


    def visitBucle(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'WHILE')
        self.nivell += 1
        self.visit(l[1])
        self.nivell -= 1

        print('  ' * self.nivell + 'DO')
        self.nivell += 1
        self.visit(l[3])
        self.nivell -= 1

        print('  ' * self.nivell + 'ENDWHILE\n')

# ---------------------------------------------------------------
    def visitAssignacion(self, ctx):
        l = list(ctx.getChildren())

        print('  ' * self.nivell + 'LET ' +
              FunxParser.symbolicNames[l[0].getSymbol().type] +
              '(' + l[0].getText() + ') BE:')
        self.nivell += 1
        self.visit(l[2])
        self.nivell -= 1

# ---------------------------------------------------------------
    def visitEqual(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'EQUAL(=)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitNotEqual(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'NOTEQUAL(<>)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitGreater(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'GREATER(>)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitLess(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'LESS(<)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitGreaterEqual(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'GREATEREQUAL(>=)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitLessEqual(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'GREATERLESS(<=)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

# ---------------------------------------------------------------
    def visitParentesis(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + '(')
        self.nivell += 1
        self.visit(l[1])
        self.nivell -= 1
        print('  ' * self.nivell + ')')

    def visitPotencia(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'POW(^)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitMultiplicacio(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'MULT(*)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitDivisio(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'DIV(/)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitSuma(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'ADD(+)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitResta(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'SUB(-)')
        self.nivell += 1
        self.visit(l[0])
        self.visit(l[2])
        self.nivell -= 1

    def visitLlamarFuncionCon(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'FunctionCall ' + l[0].getText()+':')
        self.nivell += 1
        self.visit(l[2])
        self.nivell -= 1

    def visitLlamarFuncionSin(self, ctx):
        l = list(ctx.getChildren())
        print('  ' * self.nivell + 'FunctionCall ' + l[0].getText()+':')

    def visitValor(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell +
              FunxParser.symbolicNames[l[0].getSymbol().type] +
              '(' + l[0].getText() + ')')

    def visitVar(self, ctx):
        l = list(ctx.getChildren())
        print("  " * self.nivell +
              FunxParser.symbolicNames[l[0].getSymbol().type] +
              '(' + l[0].getText() + ')')

# ---------------------------------------------------------------
