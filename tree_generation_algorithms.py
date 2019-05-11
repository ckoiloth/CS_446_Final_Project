from collections import deque
class Node:
    def __init__(self):
        self.contents = None
        self.children = []


class Tree:
    def __init__(self):
        self.root = Node()
        self.root.contents = "ROOT"


def insert_into_trie(root, letter):

    for i in root.children:
        if i.contents == letter:
            return i
    newChild = Node()
    newChild.contents = letter
    root.children.append(newChild)
    return newChild


def build_suffix(trie, suffix):
    current_location = trie.root
    for letter in suffix:
        current_location = insert_into_trie(current_location, letter)


def keyword_construction(filename, trie):
    f = open(filename)
    current_start = 0

    dataset = f.read()

    for i in range(current_start, len(dataset)):
        build_suffix(trie, dataset[i: len(dataset)])
        current_start += 1
    f.close()

    return trie


def print_suffix_tree(root):
    l = deque([])
    l.append(root)

    level = 0

    while len(l) > 0:
        current = l.popleft()
        print(level , current.contents)

        for i in range(len(current.children)):
            print(current.children[i].contents, end = " ", flush = True)
            l.append(current.children[i])

        print("END")
        level += 1


def tree_lookup(root, sequence):
    if root.contents == "ROOT":
        for child in root.children:
            if child.contents == sequence[0]:
                return tree_lookup(child, sequence)
        return False

    if len(sequence) == 0:
        return True

    if root.contents == sequence[0]:
        if len(sequence) == 1:
            return True
        for child in root.children:
            return tree_lookup(child, sequence[1:])

    return False


class Keyword_Node:

    def __init__(self):
        self.children = {}

def add_keyword_to_tree(root, word):
    if len(word) == 0:
        return 0

    if root.children.get(word[0]) == None:
        root.children[word[0]] = Keyword_Node()

    add_keyword_to_tree(root.children[word[0]], word[1:])

def build_keyword_tree(keywords):
    root = Keyword_Node()
    for i in range(len(keywords)):
        add_keyword_to_tree(root, keywords[i])
    return root

def follow_tree(text, start, keyword_root):
    if len(keyword_root.children) == 0:
        return True, start

    if len(text) <= start:
        return False, start

    if keyword_root.children.get(text[start]) is None:
        return False, start

    return follow_tree(text, start + 1, keyword_root.children[text[start]])

def find_in_dataset(filename, keyword_root):
    text = open(filename).read()
    allFound = []
    for i in range(len(text)):
        found, end = follow_tree(text, i, keyword_root)
        if found:
            allFound.append(text[i : end])

    return allFound




# Mcreight Algorithm
# Algorithm Based on McCreight, Edward M. "A space-economical suffix tree construction algorithm." - ACM, 1976
# Implmented using notes from :
# UH CS - 58093 String Processing Algorithms Lecture Notes
# Tested alongside PyPlot Suffix Tree for correctness
class SuffixTree():

    def __init__(self, input = ""):
        self.root = TreeNode()
        self.root.depth = 0
        self.root.idx = 0
        self.root.parent = self.root
        self.root.add_suffix_link(self.root)

        self.build(input)

    def create_node(self, x, u, d):
        i = u.idx
        p = u.parent
        v = TreeNode(idx = 1, depth = d)
        v.add_edge(u, x[i + d])
        u.parent = v
        p.add_edge(v, x[i + p.depth])
        v.parent = p
        return v

    def build(self, x):
        self.text = x
        self.build_mcCreight(x)

    def create_leaf(self, x, i, u , d):
        w = TreeNode()
        w.idx = i
        w.depth = len(x) -i
        u.add_edge(w, x[i + d])
        w.parent = u
        return w

    def build_mcCreight(self,x):
        start = self.root
        d = 0

        for i in range(len(x)):
            while start.depth == d and start.has_edges(x[d + i]):
                x = x.get_edges(x[d + i])
                d = d + 1

                while d < start.depth and x[start.idx + d] == x[i + d]:
                    d = d + 1
                if d < start.depth:
                    start = self.create_node(x, start, d)
                self.create_leaf(x, i , start, d)
                if not start.get_suffix_link():
                    self.compute_slink(x, start)
                start = start.get_suffix_link()
                d -= 1
                if d < 0:
                    d = 0

    def compute_slink(self, x, y):
        d = y.depth
        v = y.parent.get_suffix_link()

        while v.depth < d - 1:
            v = v.get_edges(x[y.idx + v.depth + 1])
        if v.depth > d - 1:
            v = self.create_node(x, v, d -1)
        y.add_suffix_link(v)


    def find(self, y):
        node = self.root

        while True:
            edge = self.get_edge_label(node, node.parent)
            if edge.startswith(y):
                break
            i = 0

            while i < len(edge) and edge[i] == y[0]:
                y = y[1 :]
                i += 1

            if i != 0 :
                if i == len(edge) and y != '':
                    pass
                else:
                    return []

            node.get_edges(y[0])
            if not node:
                return []

            leaves = node.get_leaves()
            return [n.idx for n in leaves]

    def get_edge_label(self, node, parent):
        return self.text[node.idx + parent.depth : node.idx + node.depth]

class TreeNode():

    def __init__(self, idx = -1, parentNode = None, depth = -1):
        self.suffix_link = None
        self.idx = idx
        self.depth = depth
        self.parent = parentNode
        self.edges = []

    def get_edges(self, suffix):
        for node, _suffix in self.edges:
            if _suffix == '$' or suffix == _suffix:
                return node
        return False

    def add_edge(self, node, suffix = ''):
        l = self.get_edges(suffix)
        if l:
            self.edges.remove((l,suffix))
        self.edges.append((node, suffix))

    def add_suffix_link(self, node):
        self.suffix_link = node

    def get_suffix_link(self):
        if self.suffix_link is not None:
            return self.suffix_link
        else:
            return False

    def has_edges(self, suffix):
        for node, _suffix in self.edges:
            if _suffix == '$' or suffix == _suffix:
                return True
        return False
    def get_leaves(self):
        if len(self.edges) == 0:
            return [self]
        return [x for (n,y) in self.edges for x in n.get_leaves()]

