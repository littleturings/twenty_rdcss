node_list = [
    {'data': 'A', 'left': 'B', 'right': 'C', 'is_root': True},
    {'data': 'B', 'left': 'D', 'right': 'E', 'is_root': False},
    {'data': 'D', 'left': None, 'right': None, 'is_root': False},
    {'data': 'E', 'left': 'H', 'right': None, 'is_root': False},
    {'data': 'H', 'left': None, 'right': None, 'is_root': False},
    {'data': 'C', 'left': 'F', 'right': 'G', 'is_root': False},
    {'data': 'F', 'left': None, 'right': None, 'is_root': False},
    {'data': 'G', 'left': 'I', 'right': 'J', 'is_root': False},
    {'data': 'I', 'left': None, 'right': None, 'is_root': False},
    {'data': 'J', 'left': None, 'right': None, 'is_root': False},
]

class Node:
    def __init__(self,data,left=None,right=None):
        self.data,self.right,self.left = data,right,left

class Tree:
    def __init__(self,root=None):
        self.root = root
    def init_data(self,datas):
        node_dict = {}
        for d in datas:
            node = Node(d['data'],d['left'],d['right'])
            node_dict[d['data']] = node
        for d in datas:
            node = node_dict[d['data']]
            if node.left:
                node.left = node_dict[node.left]
            if node.right:
                node.right = node_dict[node.right]
            if d['is_root']:
                self.root = node
    def iter_node1(self,node):
        if node:
            print(node.data)
            self.iter_node1(node.left)
            self.iter_node1(node.right)
    def iter_node2(self,node):
        node_list =[node]
        for n in node_list:
            print(n.data)
            if n.left:
                node_list.append(n.left)
            if n.right:
                node_list.append(n.right)
    def reverse(self,node):
        if node:
            node.left ,node.right = node.right,node.left
            self.reverse(node.left)
            self.reverse(node.right)

if __name__ == "__main__":
    
    tree = Tree()
    tree.init_data(node_list)
    tree.reverse(tree.root)
    # tree.iter_node1(tree.root)
    tree.iter_node2(tree.root)