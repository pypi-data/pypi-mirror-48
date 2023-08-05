import astor
import ast

from typing import List, Tuple

import inspect
import textwrap

from .tree_walk import TreeWalk


ast_string = {
    ast.Gt: '<',
    ast.GtE: '<=',
    ast.Lt: '>',
    ast.LtE: '>=',
    ast.NotEq: '!=',
    ast.Eq: '==',
    ast.And: 'and',
    ast.Or: 'or',
    ast.Add: '+',
    ast.Sub: '-',
    ast.Mult: '*',
    ast.Div: '/',
    ast.FloorDiv: '//',
    ast.Mod: '%',
    ast.LShift: '<<',
    ast.RShift: '>>',
    ast.BitAnd: '&',
    ast.BitOr: '|',
    ast.BitXor: '^',
}

ast_op_name = {
    ast.Gt: 'gt',
    ast.GtE: 'gte',
    ast.Lt: 'lt',
    ast.LtE: 'lte',
    ast.NotEq: 'noteq',
    ast.Eq: 'eq',
    ast.And: 'and',
    ast.Or: 'or',
}


def increment(number):
    return ast.copy_location(ast.Num(number.n + 1), number)


def decrement(number):
    return ast.copy_location(ast.Num(number.n - 1), number)


def minus(number):
    return ast.copy_location(ast.Num(-1 * number.n), number)


def to_string(op):
    for ast_node, string in ast_string.items():
        if isinstance(op, ast_node):
            return string


def to_op_name(op):
    for ast_node, op_name in ast_op_name.items():
        if isinstance(op, ast_node):
            return op_name


def to_ast_node(op_string):
    for ast_node, string in ast_string.items():
        if op_string == string:
            return ast_node()


def get_function_object(ast_node, function_name):
    namespace = {}
    exec(ast_to_executable(ast_node), globals(), namespace)
    return namespace[function_name]


def function_to_ast_node(function):
    code = textwrap.dedent(inspect.getsource(function))
    module = ast.parse(code)
    return list(astor.iter_node(module))[0][0][0]


def ast_to_executable(ast_expr):
    return compile(ast.Module(body=[ast_expr]), '', 'exec')


def print_ast(node):
    print(astor.to_source(node))
