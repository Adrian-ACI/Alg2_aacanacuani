# Python program to demonstrate searching operation
# in binary search tree without recursion
class newNode:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to check the given
# key exist or not


def iterativeSearch(root, key):

    # Traverse until root reaches
    # to dead end
    while root != None:

        # pass right subtree as new tree
        if key > root.data:
            root = root.right

        # pass left subtree as new tree
        elif key < root.data:
            root = root.left
        else:
            return True  # if the key is found return 1
    return False

# A utility function to insert a
# new Node with given key in BST


def insert(Node, data):

    # If the tree is empty, return
    # a new Node
    if Node == None:
        return newNode(data)

    # Otherwise, recur down the tree
    if data < Node.data:
        Node.left = insert(Node.left, data)
    elif data > Node.data:
        Node.right = insert(Node.right, data)

    # return the (unchanged) Node pointer
    return Node


# Driver Code
if __name__ == '__main__':

    # Let us create following BST
    # 50
    # 30	 70
    # / \ / \
    # 20 40 60 80
    root = None
    raiz = int(
        input("Ingrese el valor raiz para la generacion del arbol binario: "))
    nodosNum = int(
        input("Cantidad de nodos para la generacion del arbol binario: "))
    root = insert(root, raiz)
    nodo = ""
    for i in range(nodosNum-1):
        insert(root, int(input(f"Ingrese el valor {i+1}: ")))

    if iterativeSearch(root, int(
            input("Valor a buscar en arbol: "))):
        print("Yes")
        print(iterativeSearch(root, 12))

    else:
        print("No")


# This code is contributed by PranchalK
