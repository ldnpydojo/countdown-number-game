import sys
from operator import add, sub, div, mul

OPS = {
    add: ('+', sub),
    sub: ('-', add),
    mul: ('*', div),
    div: ('/', mul),
    }

def get_inverse_op(op):
    return OPS[op][1]

def get_op_sym(op):
    return OPS[op][0]

def f(target, nos_avail):
    if target in nos_avail:
        return '%d' % target

    for no in nos_avail:
        for op in OPS.keys():
            new_target = get_inverse_op(op)(target, no)
            if op == mul and target % no != 0:
                continue
            new_nos_available = [x for x in nos_avail if x != no]
            result = f(new_target, new_nos_available)
            if result:
                return '(%s) %s %s' % (result, get_op_sym(op), no)

    return None

target = int(sys.argv[1])
nos = [int(x) for x in sys.argv[2:]]

expr = f(target, nos)
if expr:
    print '%s = %s' % (target, expr)
    if  eval(expr) == target:
        print 'CORRECT'
    else:
        print 'FAIL'
else:
    print "No solution"
