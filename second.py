from collections import namedtuple

# Node namedtuple with 2 parameters: value, parent
Node = namedtuple('Node', ['value', 'parent'])

a = Node(1, 0)
b = Node(2, 1)
c = Node(3, 1)
d = Node(4, 2)
e = Node(5, 2)
f = Node(6, 3)
g = Node(7, 3)
h = Node(8, 4)
i = Node(9, 4)
# list of all node tree items
tree = [a, b, c, d, e, f, g, h, i]


def ancestors(node, tree):
    '''
    Finds all node ancesters
    '''
    while True:
        # used to return node item
        yield node

        node = find_parent_node(node, tree)
        # if parent node is not found, finish loop
        if not node:
            break
        ancestors(node, tree)


def find_parent_node(node, tree):
    '''
    Find parent node for current node item
    Returns: node item or None
    '''
    nodes = list(filter(lambda x: x.value == node.parent, tree))
    return nodes[0] if nodes else None


def lca(a, b, tree):
    '''
    Main function that returns closest common ancestor
    '''
    ancestors_a = list(ancestors(a, tree))
    ancestors_b = list(ancestors(b, tree))

    common = [i for i in ancestors_a if i in ancestors_b]

    return common[0] if common else None


print(lca(i, h, tree))
