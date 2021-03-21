# returns whether s is int
def is_int(s):
    try:
        int(s)
        return True
    except:
        return False

# get expression and chars
exp = input('Enter a postfix expression: ')
chs = exp.split()

stack = []
for ch in chs:
    # if int, add to stack
    if is_int(ch):
        num = int(ch)
        stack.append(num)
    # if operator, evaluate stack
    else:
        b = stack.pop()
        a = stack.pop()
        if ch == '+': stack.append(a + b)
        elif ch == '-': stack.append(a - b)
        elif ch == '*': stack.append(a * b)
        elif ch == '/': stack.append(a / b)

print(stack[0])
