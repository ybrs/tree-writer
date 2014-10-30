
class Node(object):

    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        self.children.extend(args)

    def __repr__(self):
        return "<Node %s>" % self.name

class TreeDraw(object):

    def __init__(self, root):
        self.root = root
        self.widths = {}

    def calc_max_width(self, line=0, tail=None):
        if not tail:
            tail = [root]

        self.widths[line] = 0
        next_tail = []

        any_has_child = False
        for node in tail:
            if node.children:
                self.widths[line] += len(node.children)
                for child in node.children:
                    next_tail.append(child)
                any_has_child = True
            else:
                self.widths[line] += 1
                next_tail.append(node)
        l = line + 1
        if any_has_child:
            self.calc_max_width(l, next_tail)


if __name__ == "__main__":
    """

    for a given graph it should draw something like this
     _________
    | a  b  c |
    |    |    |
    |  d   e  |

    """

    root = Node('root')
    a = Node('a')
    b = Node('b')
    c = Node('c')
    root.add_children(a, b, c)
    d = Node('d')
    e = Node('e')
    b.add_child(d)
    b.add_child(e)

    td = TreeDraw(root)
    td.calc_max_width()
    print td.widths