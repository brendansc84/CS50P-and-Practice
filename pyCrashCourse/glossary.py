functions = {
    'for': 'to loop through items in a list/dict',
    'if': 'looks for certain params to execute another function',
    'list': 'a list of items using []',
    'dict': 'dictionary; contains {key: value}',
    'variable': 'assigned specific values to call'
    }

functions['int'] = 'integer - whole numbers'
functions['float'] = 'number(s) with decimals'
functions['while'] = 'another loop, while x exists do y'
functions['print'] = 'have python write x'
functions['+='] = 'n = n + x -> quick way to concatenate'

for function, value in functions.items():
    print(f"{function}: {value}")