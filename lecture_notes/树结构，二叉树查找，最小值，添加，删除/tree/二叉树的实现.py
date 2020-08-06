node_list = [
    {'data': 60, 'left': 12, 'right': 90, 'is_root': True},
    {'data': 12, 'left': 4, 'right': 41, 'is_root': False},
    {'data': 4, 'left': 1, 'right': None, 'is_root': False},
    {'data': 1, 'left': None, 'right': None, 'is_root': False},
    {'data': 41, 'left': 29, 'right': None, 'is_root': False},
    {'data': 29, 'left': 23, 'right': 37, 'is_root': False},
    {'data': 23, 'left': None, 'right': None, 'is_root': False},
    {'data': 37, 'left': None, 'right': None, 'is_root': False},
    {'data': 90, 'left': 71, 'right': 100, 'is_root': False},
    {'data': 71, 'left': None, 'right': 84, 'is_root': False},
    {'data': 100, 'left': None, 'right': None, 'is_root': False},
    {'data': 84, 'left': None, 'right': None, 'is_root': False},
]
class Node:
    def __init__(self,data,left=None,right=None):
        self.data,self.right,self.left = data,right,left
    def __str__(self):
        return '数据是：{}'.format(self.data)
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
    def search(self,subtree,value):
        if subtree is None:
            return None
        elif subtree.data > value:
            return self.search(subtree.left,value)
        elif subtree.data < value:
            return self.search(subtree.right,value)
        else:
            return subtree

    def get_min(self,subtree):
        if subtree is None:
            return None
        elif subtree.left is None:
            return subtree
        else:
            return self.get_min(subtree.left)
    
    def insert_data(self,subtree,value):
        if subtree is None:
            subtree = Node(value)
        elif subtree.data > value:
            subtree.left = self.insert_data(subtree.left,value)
        else:
            subtree.right = self.insert_data(subtree.right,value)
        return subtree
    def add(self,value):
        # 查找数据  是否已存在
        node = self.search(self.root,value)
        if node:
            return False
        else:
            self.root = self.insert_data(self.root,value)
            return True

    def remove_node(self,subtree,value):
        if subtree is None:
            return None
        elif subtree.data > value:
            subtree.left = self.remove_node(subtree.left,value)
            return subtree
        elif subtree.data < value:
            subtree.right = self.remove_node(subtree.right,value)
        else:
            # 找到数据节点 ： 1，2，3
            if subtree.left is None and subtree.right is None:
                return None
            elif subtree.left is None or subtree.right  is None:
                if subtree.left is not None:
                    return subtree.left
                else:
                    return subtree.right
            else:
                node = self.get_min(subtree.right)
                subtree.data =  node.data
                subtree.right = self.remove_node(subtree.right,node.data)
                return subtree

        
        
    def remove(self,value):
        # 判断树中是否包含要删除的数据
        if self.search(self.root,value):
            self.remove_node(self.root,value)
            return True
        return False


if __name__ == "__main__":
    tree= Tree()
    # tree.init_data(node_list)
   
    # print(tree.search(tree.root,41).data)
    # print(tree.search(tree.root,55))
    # print(tree.get_min(tree.root))

    tree.add(60)
    tree.add(12)
    tree.add(90)
    tree.add(4)
    tree.add(41)
    tree.add(71)
    tree.add(100)
    tree.add(1)
    tree.add(29)
    tree.add(84)
    tree.add(23)
    tree.add(37)

    tree.remove(15)
    # print(tree.root.data)
    # print(tree.root.left)
    # tree.remove(12)
    # print(tree.root.data)
    # print(tree.root.left)

