"""
https://www.hackerrank.com/challenges/simple-text-editor/problem

Assumption
No delete operation if the stack is empty
No undo operation in the beginning

"""


def execute_action(editor, history_stack, operation, subject=None, save_history=True):
    if operation == 1:
        for ch in subject:
            editor.append(ch)
        if save_history:
            history_stack.append([2, len(subject)])
    if operation == 2:
        if save_history:
            history_stack.append([1, editor[-subject:]])
        for y in xrange(subject):
            editor.pop(-1)
    if operation == 3:
        print editor[subject-1]
    if operation == 4:
        operation, subject = history_stack.pop(-1)
        execute_action(editor, history_stack, operation, subject, save_history=False)


no_of_oper = int(raw_input().strip())
history_stack = []
editor = []
for oper_no in xrange(no_of_oper):
    inp = raw_input().strip()
    if inp == '4' or inp == 4:
        operation = 4
        subject = None
    else:
        inp = inp.split(' ')
        operation = int(inp[0])
        if operation != 1:
            subject = int(inp[1])
        else:
            subject = inp[1]

    execute_action(editor, history_stack, operation, subject)
