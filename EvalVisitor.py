if __name__ is not None and "." in __name__:
    from .FunxParser import FunxParser
    from .FunxVisitor import FunxVisitor
else:
    from FunxParser import FunxParser
    from FunxVisitor import FunxVisitor


class Function:
    def __init__(self, params, codigo):
        self.params = params
        self.codigo = codigo


class EvalVisitor(FunxVisitor):
    def __init__(self, functionMap):
        self.stack = [{}]
        self.functionMap = functionMap

# ---------------------------------------------------------------

    def visitRoot(self, ctx: FunxParser.RootContext):
        result = None
        for func in ctx.function():
            self.visit(func)
        if ctx.expression():
            result = self.visit(ctx.expression())

        return (result, self.functionMap)

# ---------------------------------------------------------------

    def visitFunction(self, ctx):
        child = list(ctx.getChildren())
        params = self.visit(child[1])
        inst = []
        for i in range(3, len(child)-1):
            inst.append(child[i])
        self.functionMap[child[0].getText()] = Function(params, inst)

    def visitParameters(self, ctx):
        child = list(ctx.getChildren())
        params = []
        for i in range(0, len(child)):
            params.append(child[i].getText())
        return params

# ---------------------------------------------------------------

    def visitIfElse(self, ctx):
        child = list(ctx.getChildren())
        if (self.visit(child[1])):
            self.visit(child[3])
        else:
            self.visit(child[7])
        return None

    def visitIf(self, ctx):
        child = list(ctx.getChildren())
        if (self.visit(child[1])):
            return self.visit(child[3])

# ---------------------------------------------------------------

    def visitLoop(self, ctx):
        child = list(ctx.getChildren())
        while (self.visit(child[1])):
            self.visit(child[3])
        return None

# ---------------------------------------------------------------

    def visitEqual(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) == self.visit(child[2])

    def visitNotEqual(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) != self.visit(child[2])

    def visitGreater(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) > self.visit(child[2])

    def visitLess(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) < self.visit(child[2])

    def visitGreaterEqual(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) >= self.visit(child[2])

    def visitLessEqual(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) <= self.visit(child[2])

# ---------------------------------------------------------------

    def visitAssignation(self, ctx):
        child = list(ctx.getChildren())
        level = len(self.stack)-1
        self.stack[level][child[0].getText()] = self.visit(child[2])
        return None

# ---------------------------------------------------------------

    def visitCallFunction(self, ctx):
        child = list(ctx.getChildren())
        f = self.functionMap.get(child[0].getText())
        if (f is None):
            raise Exception("The function: " + child[0].getText() +
                            ",does not exist")

        if (len(f.params) != len(child)-1):
            raise Exception('The number of parameters does not match.\
                            Expected: ' + str(len(f.params)) +
                            '.Actual: ' + str(len(child)-1))

        newdict = {}
        for i in range(0, len(f.params)):
            newdict[f.params[i]] = self.visit(child[i+1])
        self.stack.append(newdict)

        result = None
        for inst in f.codigo:
            result = self.visit(inst)
            if result is not None:
                break

        self.stack.pop()
        return result

    def visitArguments(self, ctx):
        child = list(ctx.getChildren())
        params = []
        for i in range(0, len(child)):
            params.append(self.visit(child[i]))
        return params

# ---------------------------------------------------------------

    def visitParentesis(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[1])

    def visitPower(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) ** self.visit(child[2])

    def visitMultiplication(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) * self.visit(child[2])

    def visitDivision(self, ctx):
        child = list(ctx.getChildren())
        div = self.visit(child[2])
        if div == 0:
            raise Exception("Can not divide by 0")
        return self.visit(child[0]) / self.visit(child[2])

    def visitModulus(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) % self.visit(child[2])

    def visitPlus(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) + self.visit(child[2])

    def visitMinus(self, ctx):
        child = list(ctx.getChildren())
        return self.visit(child[0]) - self.visit(child[2])

    def visitValor(self, ctx):
        child = list(ctx.getChildren())
        return int(child[0].getText())

    def visitVariable(self, ctx):
        child = list(ctx.getChildren())
        varName = child[0].getText()
        level = len(self.stack)-1
        var = self.stack[level].get(varName)
        if var is None:
            raise Exception("The variable:" + varName +
                            " does not exist")
        return var

# ---------------------------------------------------------------
