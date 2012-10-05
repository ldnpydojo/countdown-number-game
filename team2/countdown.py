import random
from operator import add, sub, mul, div

NUMBER_NUMBERS = 6
NUMBER_BIG = 2
NUMBER_SMALL = NUMBER_NUMBERS - NUMBER_BIG

BIG_NUMBERS = [n for n in range(25, 125, 25)]
SMALL_NUMBERS = range(1, 11)
OPERATORS = [add, sub, mul, div]
TARGET = random.randint(100, 999)

tiles = random.sample(BIG_NUMBERS, NUMBER_BIG) + random.sample(SMALL_NUMBERS, NUMBER_SMALL)
print 'try to get to', TARGET, 'using', tiles

class Node(object):
    def __init__(self, n, m, op):
        self.n = n
        self.m = m
        self.op = op
    
    def __str__(self):
        n = str(self.n)+', ' if isinstance(self.n, Node) else self.n
        m = str(self.m)+', ' if isinstance(self.m, Node) else self.m
        return '{0} {1} {2} = {3}'.format(n, self.op.__name__, m, self.calc())
    
    def calc(self):
        n = self.n.calc() if isinstance(self.n, Node) else self.n
        m = self.m.calc() if isinstance(self.m, Node) else self.m
        return self.op(n, m)
        
# n = Node(tiles[0], tiles[1], add)
# m = Node(tiles[2], n, add)
# print m.calc()
start_tiles = tiles[:]
layer = [(Node(0,0,add),tiles)]
def walk_tree(this_layer):
    next_layer = []
    if len(this_layer[0][1]) == 0:
           #done
           return this_layer
    print 'this layer has', len(this_layer[0][1]), 'tiles'
    for node, tiles in this_layer:
        # print 'node is -', node, ' tiles are -', tiles
        for i in tiles:   
            tiles_left = tiles[:]
            # print 'i is',i
            tiles_left.remove(i)
            # print ' : '.join([str(x) for x in tiles_left])
            for oper in OPERATORS:
                #yield next_layer((Node(i,j,oper), tiles_moving_on))
                if oper != div or (node.calc() % i) == 0:
                    next_layer.append((Node(node,i,oper), tiles_left))
    return walk_tree(next_layer)

def solver(ans):
    return abs(TARGET-ans.calc())

#numbers = [l.calc() for l in layer]
#print ' : '.join([str(i) for i in layer])
#print numbers

leaves = [node for (node, tiles) in walk_tree(layer) if len(tiles)==0]
best = min(leaves, key=solver)

print 'target was', TARGET
print 'tiles were', start_tiles
print 'best answer - ', best