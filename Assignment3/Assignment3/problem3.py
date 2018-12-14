import sys

class RbNode:

    def __init__(self, key, left=None, right=None, p=None, color='black'):
        self.key = key
        self.left, self.right = left, right
        self.p = p
        self.color = color

    def __repr__(self):
        return '{}'.format(self.key)

    def __int__(self):
        return int(self.key)

class RbTree:
    # note: it's very subtle that nil.p may change, keep it in mind
    @property
    def nil(self):
        node = getattr(self, '_nil_node', None)
        if node:
            return node
        nil = RbNode('nil')
        nil.left = nil.right = nil.p = nil
        nil.color = 'black'
        self._nil_node = nil
        return nil

    def __init__(self):
        self.root = self.nil
        self.size = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left  # x
        if y.left is not self.nil:  # y.left
            y.left.p = x
        y.p = x.p  # y
        if x.p is self.nil:  # x.p
            self.root = y
        elif x is x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x  # y
        x.p = y  # x

    def right_rotate(self, x):
        y = x.left
        x.left = y.right  # y
        if y.right is not self.nil:  # x.right
            y.right.p = x
        y.p = x.p  # x
        if x.p is self.nil:  # y.p
            self.root = y
        elif x is x.p.right:
            x.p.right = y
        else:
            x.p.left = y
        y.right = x  # x
        x.p = y  # y

    def rb_insert(self, key):
        current = self.root
        p = self.nil
        self.size +=1
        while current is not self.nil:
            p = current
            if current.key - key <= 0:
                current = current.right

            elif current.key-key > 0:
                current = current.left

        newNode = RbNode(key=key, color='red', p=self.nil, left=self.nil, right=self.nil)
        newNode.p = p

        if p is self.nil:  # self.root is self.nil
            self.root = newNode
        elif key >= p.key:
            p.right = newNode
        else:
            p.left = newNode
        self.rb_insert_fixup(newNode)

    def rb_insert_fixup(self, node):
        while node != self.root and node.p.color == 'red':
            father = node.p
            if father is father.p.left:
                uncle = father.p.right
                if uncle.color == 'red':  # case 1
                    father.color = uncle.color = 'black'
                    father.p.color = 'red'  # maintain black-height equal property
                    node = father.p  # because this node color change to red, maybe it will destory rule
                    #continue
                # only after case1 operation, case2 and case3 may happen
                else:
                    if father.right is node:  # case 2, node is right child of it's parent
                        node = father
                        self.left_rotate(node)  # left rotate to case 3
                # case 3, node is left child of it's parent
                    node.p.color = 'black'
                    node.p.p.color = 'red'
                    self.right_rotate(node.p.p)
                # after case2 and case3, the loop condition will not satisified to quit
            else:  # node.p is node.p.p.right
                uncle = father.p.left
                if uncle.color == 'red':  # case 1
                    father.color = uncle.color = 'black'
                    father.p.color = 'red'
                    node = father.p
                    continue
                else:
                    if father.left is node:  # case 2
                        node = father
                        self.right_rotate(node)

                    node.p.color = 'black'  # case 3
                    node.p.p.color = 'red'
                    self.left_rotate(node.p.p)

        self.root.color = 'black'  # here root cannot be nil

    # search
    def rb_search(self, key):
        current = self.root
        if current is self.nil:
            return None
        while current is not self.nil:
            if current.key == key:
                return current
            elif current.key - key > 0:
                current = current.left
            elif current.key <= key:
                current = current.right
        return current

    # remove
    def rb_transplant(self, u, v):  # transplant v to u
        # absolutely transplant, just need to change two pointer(eg: u.p.child and v.p)
        if u.p == self.nil:
            self.root = v
        elif u == u.p.left:
            u.p.left = v
        else:
            u.p.right = v
        v.p = u.p

    def rb_delete(self, node):
        if node is None:
            print("TreeError")
            return
        y = node
        y_origin_color = y.color
        self.size -=1
        if node.left == self.nil:
            x = node.right
            self.rb_transplant(node, node.right)
        elif node.right == self.nil:
            x = node.left
            self.rb_transplant(node, node.left)
        else:
            y = self.tree_maximum(node.left)
            y_origin_color = y.color
            x = y.left
            if y.p == node:
                x.p = y
            else:
                self.rb_transplant(y, y.left)
                y.left = node.left
                y.left.p = y
            self.rb_transplant(node, y)
            y.right = node.right
            y.right.p = y
            y.color = node.color
        if y_origin_color == 'black':
            self.rb_delete_fixup(x)

    def rb_delete_fixup(self, node):
        while node is not self.root and node.color == 'black':
            if node is node.p.left:
                brother = node.p.right
                if brother.color == 'red':  # case 1, after case 1, it can be case 2, 3, 4
                    brother.color = 'black'
                    node.p.color = 'red'
                    self.left_rotate(node.p)
                    brother = node.p.right
                # brother must be black now
                if brother.left.color == 'black' == brother.right.color:  # case 2, after case 2, it can be case 1, 2, 3, 4
                    brother.color = 'red'
                    node = node.p
                   #continue
                else:
                    if brother.right.color == 'black':  # case 3, after this, it can only be case 4
                        brother.left.color = 'black'
                        brother.color = 'red'
                        self.right_rotate(brother)
                        brother = node.p.right
                    brother.color = node.p.color
                    node.p.color = 'black'
                    brother.right.color = 'black'
                    self.left_rotate(node.p)
                    node = self.root
                    break
            else:
                brother = node.p.left
                if brother.color == 'red':  # case 1
                    brother.color = 'black'
                    node.p.color = 'red'
                    self.right_rotate(node.p)
                    brother = node.p.left
                if brother.left.color == 'black' == brother.right.color:  # case 2
                    brother.color = 'red'
                    node = node.p
                    #continue
                else:
                    if brother.left.color == 'black':  # case 3
                        brother.color = 'red'
                        brother.right.color = 'black'
                        self.left_rotate(brother)
                        brother = node.p.left
                        # case 4, after case 4, everything will be satisfied
                    brother.color = node.p.color
                    brother.left.color = 'black'
                    node.p.color = 'black'
                    self.right_rotate(node.p)
                    node = self.root
                    break
        node.color = 'black'

    def tree_maximum(self, node):
        current = node
        while current.right is not self.nil:
            current = current.right
        if current is self.nil:
            return None
        return current

    def tree_minimum(self, node):
        current = node
        while current.left is not self.nil:
            current = current.left
        if current is self.nil:
            return None
        return current

    def inorder(self, x):
        if x != self.nil:
            self.inorder(x.left)
            print(x.key,)
            self.inorder(x.right)

    def rb_print(self):
        if self.root == self.nil:
            print("Empty")
        #self.Inorder_Tree_Walk(self.root)
        else:
            self.inorder(self.root)
            print("!!!root: ",self.root)

    def treeSize(self, root):
        if root is self.nil:
            return 0
        else:
            return 1 + self.treeSize(root.left) + self.treeSize(root.right)


minRb = RbTree()
maxRb = RbTree()

def insert(item):
    if minRb.root is minRb.nil or item < -minRb.tree_minimum(minRb.root).key:
        minRb.rb_insert(-item)  # make negative for being min heap
        rebalance()
    else:
        maxRb.rb_insert(item)
        rebalance()


def delete(item):
    mn = minRb.rb_search(-item)
    mx = maxRb.rb_search(item)
    if mn is not minRb.nil:
        minRb.rb_delete(mn)
        rebalance()
    else:
        maxRb.rb_delete(mx)
        rebalance()

def rebalance():
    #first_len = minRb.treeSize(minRb.root)
    first_len = minRb.size
    #second_len = maxRb.treeSize(maxRb.root)
    second_len = maxRb.size
    if first_len - second_len > 1:
        elt = minRb.tree_minimum(minRb.root)    # pop smallest(actually largest) and push into max heap
        minRb.rb_delete(elt)
        maxRb.rb_insert(-elt.key)
    elif second_len - first_len > 1:
        elt = (maxRb.tree_minimum(maxRb.root))
        maxRb.rb_delete(elt)
        minRb.rb_insert(-elt.key)

def median():
    #first_len = minRb.treeSize(minRb.root)
    first_len = minRb.size
    #second_len = maxRb.treeSize(maxRb.root)
    second_len = maxRb.size
    if first_len > second_len:
        result = -minRb.tree_minimum(minRb.root).key
    elif second_len > first_len:
        result = maxRb.tree_minimum(maxRb.root)
    else:
        result = -minRb.tree_minimum(minRb.root).key + maxRb.tree_minimum(maxRb.root).key
        if result % 2 == 0:
            result = result//2
        else:
            result = round((result/2.0), 1)
    return result

def driver():
    with open(sys.argv[1]) as f:
    #with open(input("Enter Filename: "), 'r') as f:
        n = int(f.readline().strip())
        for _ in range(n):
            in_data = f.readline().strip().split()
            command, key = in_data[0], in_data[1:]
            k = int(key[0])
            if command == "add":
                insert(k)
                print(median())
            elif command == "remove":
                delete(k)
                print(median())


if __name__ == '__main__':
    driver()