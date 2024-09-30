def brackets_counter(string):
    stack = []
    open_brackets = '([{'
    close_brackets = ')]}'
    for char in string:
        if char not in open_brackets + close_brackets:
            continue
        if char in open_brackets:
            stack.append(char)
        elif char in close_brackets:
            if not stack:
                return 'Not symmetrical'
            if open_brackets.index(stack[-1]) == close_brackets.index(char):
                stack.pop()
            else:
                return 'Not symmetrical'
    return 'Symmetrical' if not stack else 'Not symmetrical'


print(brackets_counter('(1ssf){something[[{}]]}'))
print(brackets_counter('{[[{]]'))
print(brackets_counter('(((( ){[ 1 ]( 1 + 3 )( ){ }}'))
print(brackets_counter(')'))
print(brackets_counter('( ){[ 1 ]( 1 + 3 )( ){ }}'))
