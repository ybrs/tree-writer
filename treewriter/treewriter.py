from collections import defaultdict
class Node(object):

    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_children(self, *args):
        self.children.extend(args)

    def __repr__(self):
        return "<Node %s x:%s>" % (self.name, self.x)

node_width = 3

class TreeDraw(object):

    def __init__(self, root):
        self.root = root
        self.widths = {}
        self.lines = defaultdict(list)

    def draw(self):
        from blessings import Terminal
        term = Terminal()

        for x in range(0,120):
            for y in range(0, 10):
                with term.location(x=x, y=y):
                    print " "

        for line, nodes in self.lines.iteritems():
            for node in nodes:
                with term.location(y=line + 1, x=node.x+10):
                    print term.bold + "|%s|" % node.name

        with term.location(y=line+3, x=0):
            print ">>> max width:", max(self.widths.values())


    def calc_max_width(self, line=0, tail=None):
        if not tail:
            tail = [root]
        self.widths[line] = 0
        next_tail = []
        any_has_child = False
        last_x = 0
        for node in tail:
            node.x = last_x
            if node.children:
                self.widths[line] += len(node.children)
                for child in node.children:
                    next_tail.append(child)
                    self.lines[line].append(child)
                    child.x += node.x + node_width
                    last_x += node_width
                any_has_child = True
            else:
                node.x = last_x
                self.widths[line] += node_width
                next_tail.append(node)
                last_x += node_width

        if any_has_child:
            l = line + 1
            self.calc_max_width(l, next_tail)


if __name__ == "__main__":
    """

    for a given graph it should draw something like this

    |___________|
    | a   b   c | 0
    |     |     |
    |   d   e   | 1

    """

    root = Node('root')
    a = Node('a')
    b = Node('b')
    c = Node('c')
    g = Node('g')
    h = Node('h')
    root.add_children(a, b, c, g, h)

    d = Node('d')
    e = Node('e')
    z = Node('z')
    c.add_children(d, e, z)
    z.add_children(Node('F'), Node('I'))

    one = Node(1)
    two = Node(2)
    h.add_children(one, two, Node("T"))
    two.add_children(Node("3"), Node("4"), Node("R"))
    nine = Node(9)
    one.add_children(Node("8"), nine, Node("U"))
    nine.add_children(Node("7"), Node("G"))

    td = TreeDraw(root)
    td.calc_max_width()
    print td.widths
    print td.lines
    td.draw()
    print len("|___________|")

    exit()

    # """
    # |___________|
    # | a  b  c   |
    # |       |   |
    # |     d   e |
    #
    # """
    # root = Node('root')
    # a = Node('a')
    # b = Node('b')
    # c = Node('c')
    # root.add_children(a, b, c)
    # d = Node('d')
    # e = Node('e')
    # c.add_child(d)
    # c.add_child(e)
    # td = TreeDraw(root)
    # td.calc_max_width()
    # print td.widths
    # print len("|___________|")

    """

    for a given graph it should draw something like this

    |_______________|
    | a    b     c  |
    |      |        |
    |    d    e     |
    |         |     |
    |       f   g   |
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
    f = Node('f')
    g = Node('g')
    e.add_children(f, g)

    td = TreeDraw(root)
    td.calc_max_width()
    print td.widths
    print td.lines
    print len("|_______________|")
