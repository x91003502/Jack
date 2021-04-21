
s1 = "(())"
s2 = "(()))"
s3 = "()((((())()()))))"
s4 = "(())())()()((()(()))))"
def balanced_brackets(s):
    stack = []
    if len(s) == 0:
        print('Empty String.')
        return
    balanced = False
    for i in range(len(s)):
        if s[i] == ")" and len(stack) > 0:
            stack.pop()
        elif s[i] == ")" and len(stack) == 0:
            print(f'Is Balanced : {False}')
            return False
        else:
            stack.append(s[i])
    if len(stack) == 0:
        balanced = True
    print(f'Is Balanced : {balanced}')
    return balanced

balanced_brackets(s1)
balanced_brackets(s2)
balanced_brackets(s3)
balanced_brackets(s4)