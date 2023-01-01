Expr: Funx.g4
	antlr4 -Dlanguage=Python3 -no-listener  Funx.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g4

all: Funx.g4
	antlr4 -Dlanguage=Python3 -no-listener  Funx.g4
	antlr4 -Dlanguage=Python3 -no-listener -visitor Funx.g4
	clear && python3 test.py

