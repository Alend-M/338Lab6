import sys
import operator

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_expression(expression):
    #Note for TA: If not working please just replace the imputed - with your typed out -. PDF - doesnt work and in lab i was told just leave a note.
    ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    node_stack = []
    operator_stack = []
    for token in expression:
        if token in ops:
            operator_stack.append(ops[token])
        elif token == ')':
            right = node_stack.pop()
            left = node_stack.pop()
            op = operator_stack.pop()
            node = Node(op, left, right)
            node_stack.append(node)
        elif token not in '()':
            node_stack.append(Node(int(token)))
    return node_stack.pop()

def compute(node):
    if isinstance(node.value, int):
        return node.value
    else:
        return node.value(compute(node.left), compute(node.right))

def main():
    expression = sys.argv[1]
    expression = expression.split()
    if(expression[len(expression)-1] != ")" and len(expression) >= 2):
        expression.append(")")
        print(expression)
    tree = parse_expression(expression)
    result = compute(tree)
    print(int(result))

if __name__ == "__main__":
    main()