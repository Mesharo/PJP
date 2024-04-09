from antlr4 import *
from projektLanguageParser import projektLanguageParser

class TypeCheckVisitor(ParseTreeVisitor):
    def __init__(self):
        self.symbol_table = {}

    def visitProgram(self, ctx:projektLanguageParser.ProgramContext):
        for statement in ctx.statement():
            self.visit(statement)

    def visitStatement(self, ctx:projektLanguageParser.StatementContext):
        if ctx.getChildCount() == 0:
            return
        
        if ctx.WHILE():
            self.visit(ctx.expression())
            self.visit(ctx.statement(0))
        
        if ctx.INT() or ctx.FLOAT() or ctx.STRING() or ctx.BOOL():
            var_type = str(ctx.getChild(0))
            for identifier in ctx.IDENTIFIER():
                self.symbol_table[identifier.getText()] = var_type
        
        if ctx.READ():
            for identifier in ctx.IDENTIFIER():
                if identifier.getText() not in self.symbol_table:
                    raise Exception(f"Variable {identifier.getText()} not declared")
        
        if ctx.WRITE():
            for expression in ctx.expression():
                self.visit(expression)
        
        if ctx.IF():
            self.visit(ctx.expression())
            self.visit(ctx.statement(0))
            if ctx.ELSE():
                self.visit(ctx.statement(1))
        
        if ctx.expression(): # Expression statement
            self.visit(ctx.expression())

    def visitExpression(self, ctx:projektLanguageParser.ExpressionContext):
        if ctx.IDENTIFIER():
            identifier = ctx.IDENTIFIER().getText()
            if identifier not in self.symbol_table:
                raise Exception(f"Variable {identifier} not declared")
            return self.symbol_table[identifier]

        if ctx.literal():
            return self.visit(ctx.literal())

        if ctx.getChildCount() == 2:
            operand_type = self.visit(ctx.expression(0))
            operator = ctx.prefix.text
            if operator == '-':
                if operand_type != 'int' and operand_type != 'float':
                    raise Exception(f"Type mismatch in unary operation: {operator}{operand_type}")
                return operand_type
            elif operator == '!':
                if operand_type != 'bool':
                    raise Exception(f"Type mismatch in unary operation: {operator}{operand_type}")
                return operand_type

        if ctx.getChildCount() == 3:
            left = self.visit(ctx.expression(0))
            right = self.visit(ctx.expression(1))
            operator = ctx.bop.text
            if left != right:
                raise Exception(f"Type mismatch in binary operation: {left} {operator} {right}")
            return left

        if ctx.getChildCount() == 4:
            identifier = ctx.IDENTIFIER().getText()
            if identifier not in self.symbol_table:
                raise Exception(f"Variable {identifier} not declared")
            declared_type = self.symbol_table[identifier]
            assigned_type = self.visit(ctx.expression())
            if declared_type != assigned_type:
                raise Exception(f"Type mismatch in assignment: {declared_type} = {assigned_type}")

    def visitLiteral(self, ctx:projektLanguageParser.LiteralContext):
        if ctx.INT_LITERAL():
            return 'int'
        elif ctx.FLOAT_LITERAL():
            return 'float'
        elif ctx.BOOL_LITERAL():
            return 'bool'
        elif ctx.STRING_LITERAL():
            return 'string'