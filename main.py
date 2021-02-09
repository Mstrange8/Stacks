""" Name: Matthew Strange
    Class: CS2420
    Date: 02/08/2021
    Description: Program containing postfix and infix
    functions for calculations.
"""

from stack import Stack


def in2post(expr):
    """Takes an infix expression as an input and returns
    an equivalent postfix expression as a string"""
    if not isinstance(expr, str):
        raise ValueError
    if expr.count('(') != expr.count(')'):
        raise SyntaxError
    expr = expr.replace(' ', '')
    postfix = ''
    symbol_dict = {'(': 1, '+': 2, '-': 2, '*': 3, '/': 3}
    my_stack = Stack()
    for e in expr:
        if e == '(':
            my_stack.push(e)
        elif e.isnumeric():
            postfix += e + ' '
        elif e in ['+', '-', '*', '/']:
            while (my_stack.size() > 0 and my_stack.top() != '(' and
                   symbol_dict[my_stack.top()] >= symbol_dict[e]):
                postfix += my_stack.pop() + ' '
            my_stack.push(e)
        else:
            while my_stack.top() != '(' and my_stack.size() > 0:
                postfix += my_stack.pop() + ' '
            my_stack.pop()
    while my_stack.size() > 0:
        postfix += my_stack.pop() + ' '
    return postfix


def eval_postfix(expr):
    """Takes a postfix string as an input and returns a number"""
    if not isinstance(expr, str):
        raise ValueError
    try:
        if not isinstance(expr, str):
            raise ValueError
        my_stack = Stack()
        expr = expr.replace(" ", "")
        for e in expr:
            if e.isnumeric():
                my_stack.push(e)
            else:
                num1 = my_stack.pop()
                num2 = my_stack.pop()
                my_stack.push(str(eval(num2 + e + num1)))
        return float(my_stack.pop())
    except IndexError:
        raise SyntaxError


def main():
    """main functions outputting results"""
    with open('data.txt', "r") as f:
        expressions = f.readlines()

    for expr in expressions:
        expr = expr.strip()
        postfix = in2post(expr)
        print('infix: {}'.format(expr))
        print('postfix: {}'.format(postfix))
        print('answer: {}'.format(eval_postfix(postfix)))
        print('\n')


if __name__ == "__main__":
    main()
