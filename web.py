from antlr4 import InputStream
from antlr4 import CommonTokenStream
from FunxLexer import FunxLexer
from FunxParser import FunxParser
from EvalVisitor import EvalVisitor
from flask import Flask, render_template, request

global InOuts  # inputcode, result
global FunctionMap  # dictionary of functions saved
global FuncNames  # name of evey function(name + params)
InOuts = list()
FunctionMap = dict()
FuncNames = set()


class Main:
    app = Flask(__name__)

    from flask import render_template

    @app.route('/')
    def index():
        return render_template('index.html', error_message=None)

    @app.route('/procesar', methods=['POST'])
    def procesar():
        error = None
        try:
            codigo = str(request.form['texto'])
            input_stream = InputStream(codigo)
            lexer = FunxLexer(input_stream)
            token_stream = CommonTokenStream(lexer)
            parser = FunxParser(token_stream)
            tree = parser.root()
            evaluator = EvalVisitor(FunctionMap)
            result_map = evaluator.visit(tree)

            if result_map is not None:
                InOuts.insert(0, result_map[0])
                InOuts.insert(0, codigo)
                for name, function in result_map[1].items():
                    FunctionMap[name] = function
                    FuncNames.add(name+' '+" ".join(function.params))
        except Exception as e:
            error = str(e)
        finally:
            return render_template('index.html',
                                   funciones=FuncNames,
                                   tupla=InOuts,
                                   error_message=error)

    if __name__ == '__main__':
        app.run()
