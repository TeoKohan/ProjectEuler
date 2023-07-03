s = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
'''
HEIGHT = 15

class BinaryNode:

    def __init__(self, value, left, right) -> None:
        self.value = value
        self.max   = None
        self.left  = left
        self.right = right

N = [n for n in s.split('\n')]
N = [list(map(int, n.split())) for n in N]

def build_node(x, y):
    return BinaryNode(N[y][x], build_node(x, y+1), build_node(x+1, y+1)) if y < HEIGHT else None

def binary_max_sum(binary_tree: BinaryNode):
    if binary_tree.max == None:
        left  = 0 if binary_tree.left  == None else binary_max_sum(binary_tree.left )
        right = 0 if binary_tree.right == None else binary_max_sum(binary_tree.right)
        binary_tree.max = binary_tree.value + max(left, right)
    return binary_tree.max

root = build_node(0, 0)
print(binary_max_sum(root))