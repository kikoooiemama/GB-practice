# Created by Nikolay Pakhomov 19.07.2024
from binarytree import tree, bst, Node, build


# Деревья
# Бинарное неполное - одна ветка у узла.
# Бинарное дерево поиска (BST) - все узлы в левом поддереве меньше, а все узлы в правом поддереве больше данного узла.
# Бинарное дерево поиска - "упорядоченное дерево"

class MyMode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


a = tree(height=4, is_perfect=False)
print(a)

b = bst(height=3, is_perfect=True)
print(b)

# Вручную
c = Node(7)
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(1)
c.left.right = Node(5)
c.right.left = Node(9)
c.right.right = Node(13)
print(c)

d = build([7, 3, 11, 1, 5, 9, 3])
print(d)

f = build([7, 3, 11, 1, 5, 9, 3, None, 2, None, 6])
print(f)
