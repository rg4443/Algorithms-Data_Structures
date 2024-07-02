class UserDatabase:
    """Class that represents a user database with functionalitys of adding, searching, updating and listing users"""
    # Define a list of users that will define the user database
    def __init__(self):
        self.users = []

    # Insert a new user. The newly created user will keep the list of users sorted
    def insert(self, user):
        i = 0
        # Iterate through the users
        while i < len(self.users):
            # If the user's username is less than what it is being compared to then break
            if self.users[i].username > user.username:
                break
            # Move on to the next user (incrementing through the db)
            i += 1
        # Insert the corresponding users number based on number of iterations along with the user itself
        self.users.insert(i, user)
    
    # Go through each user and if that users username matches up with a query then return that user
    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
    
    # Updates a user
    def update(self, user):
        # Find the intended user that needs to be updated
        target = self.find(user.username)

        # Update the users info
        target.name, target.email = user.name, user.email
    
    # Returns self.users which is a list containing all users in the UserDatabase class
    def list_all(self):
        pass
        # COMMENTED SO THAT OTHER FUNCTIONS CAN OPERATE without printing a list of users
        # return self.users

class User:
    """Class that replicates a users information including a username, name, and email"""
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
    
    def __repr__(self):
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()

# Create User class instances to replicate users
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

# Create an instance of the User databse and insert the users from the above user instances
database = UserDatabase()
database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
database.insert(biraj)

# Testing line that updates a users info
database.update(User(username='siddhant', name='Siddhant U', email='siddhantu@example.com'))

# COMMENTED SO THAT OTHER FUNCTIONS CAN OPERATE
# Finds a user (test case)
# found_user = database.list_all()
# if found_user:
    # print(found_user)
# else:
    # print("User not found.")

class TreeNode():
    """Class that stores algorithms relating to binary trees"""
    # Initialize left and right subtrees as well as each nodes key
    def __init__(self, key):
        self.key, self.left, self.right = key, None, None
    
    # Returns the height of a Binary Tree (longest path from the root node to the farthest bottom node)
    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))
    
    # Returns the size of a binary tree (The amount of nodes)
    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    # Traverse in order algorithm that counts the amount of nodes in order.
    def traverse_in_order(self):
        if self is None: 
            return []
        return (TreeNode.traverse_in_order(self.left) + 
                [self.key] + 
                TreeNode.traverse_in_order(self.right))
    
    # Function that displays a binary tree visually
    def display_keys(self, space='\t', level=0):
        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return   

        # If the node does not have any children (a leaf)
        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        # If the node has children
        self.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        self.display_keys(self.left,space, level+1)    
    
    # Converts a Binary tree into a tuple.
    def to_tuple(self):
        if self is None:
            return None
        if self.left is None and self.right is None:
            return self.key
        
        return TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right)
    
    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())
    
    @staticmethod
    # Generates a binary tree based on a tuple given input
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)
        return node

def remove_none(nums):
    """Returns the binary search tree of a binary tree (removes every None element in nums)"""
    return [x for x in nums if x is not None]

def is_bst(node):
    """Determines if a binary tree is a Binary Search Tree"""
    # If node is None (meaning that the node is a child of a leaf), return True for being a bst node and 
    # None for the min and max values
    if node is None:
        return True, None, None
    
    # Recursively initialize if the left or right subtrees is a bst, as well as the min and max values 
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    # Initialize variable for when a node is bst via various factors
    is_bst_node = (is_bst_l and is_bst_r and 
                   (max_l is None or node.key > max_l) and 
                   (min_r is None or node.key < min_r))
    
    # Determine the minimum and maximum keys for each subtree
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    # Return if the node is bst or not (value is a boolean expression), along with the min and max key
    return is_bst_node, min_key, max_key

class BSTNode():
    """Class that represents a node in a Binary Search Tree"""
    # Initialize, nodes key, its value, its left, and right node, along with the parent node
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# Function used to display binary trees visually  
def display_keys(self, space='\t', level=0):
    if self is None:
        print(space*level + '∅')
        return   

    if self.left is None and self.right is None:
        print(space*level + str(self.key) + ": " + str(self.value))
        return

    self.display_keys(self.right, space, level+1)
    print(space*level + str(self.key) + ": " + str(self.value))
    self.display_keys(self.left,space, level+1)    

def insert(node, key, value):
    """Inserts nodes into a binary tree"""
    # If there is no node, create an instance from the BSTNode class
    if node is None:
        return BSTNode(key, value)
    # Else if the key to be inserted is less than the current nodes key
    elif key < node.key:
        # Insert the node into the currently selected nodes left side
        node.left = insert(node.left, key, value)
        # # Set the parent of the left child to the node
        node.left.parent = node
    # Else if the key to be inserted is greater than the current nodes keyy
    elif key > node.key:
        # Insert the node into the currently selected nodes right side
        node.right = insert(node.right, key, value)
        # Set the parent of the right child to be the node
        node.right.parent = node

    # Return the current node after insertion
    return node

# Test the insert function
tree = insert(None, jadhesh.username, jadhesh) # Binary Tree #1
insert(tree, biraj.username, biraj)
insert(tree, sonaksh.username, sonaksh)
insert(tree, aakash.username, aakash)
insert(tree, hemanth.username, hemanth)
insert(tree, siddhant.username, siddhant)
insert(tree, vishal.username, siddhant)

tree2 = insert(None, aakash.username, aakash) # Binary Tree #2
insert(tree2, biraj.username, biraj)
insert(tree2, hemanth.username, hemanth)
insert(tree2, jadhesh.username, jadhesh)
insert(tree2, siddhant.username, siddhant)
insert(tree2, sonaksh.username, sonaksh)
insert(tree2, vishal.username, vishal)

def find(node, key):
    """Finds a node in a binary tree given a node and a key"""
    # If no node is found, then return None
    if node is None:
        return None
    # If the search key matches a nodes key return it
    if key == node.key:
        return node
    # If the search key is greater than a nodes key, then recursively search the left subtree
    if key < node.key:
        return find(node.left, key)
    # If the search key is less than a nodes key, then recursively, search the right subtree
    if key > node.key:
        return find(node.right, key)
    
# Testing the find function
node = find(tree, 'hemanth')
if node:
    print("Key:", node.key)
    print("Value:", node.value)
else:
    print("Node not found")

# Function that updates a node given the input from find
def update(node, key, value):
    """Updates a node given the output from find function"""
    # Finds the target node using the find function
    target = find(node, key)
    # If the node returned from find function is not none
    if target is not None:
        # Replace the value of the target with the new value.
        target.value = value

# Testing Update Function
update(tree, 'hemanth', User('hemanth', 'Hemanth J', 'hemanthj@example.com'))

def list_all(node):
    """List all of the nodes in a binary tree"""
    if node is None:
        return []
    return list_all(node.left) + [(node.key, node.value)] + list_all(node.right)

# Testing the list_all function
print(list_all(tree))


def is_balanced(node):
    """Determines if a binary tree is balanced if one side of the subtree equals the other"""
    # If there are no nodes (meaning no binary tree then return true for balanced and 0 for the height)
    if node is None:
        return True, 0
    # Get if the left subtree is balanced along with the height
    balanced_l, height_l = is_balanced(node.left)
    # Get if the right subtree is balanced along with the height
    balanced_r, height_r = is_balanced(node.right)
    # Initialize variable that determines if a binary tree is balanced via various factors
    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    # Gets the height of the entire binary tree (adding 1 to include the root node)
    height = 1 + max(height_l, height_r)
    # Returns if the tree is balanced as well as its height.
    return balanced, height

def make_balanced_bst(input, lo=0, hi=None, parent=None):
    """Creates balanced binary search trees"""
    # Define the high index if none is provided
    if hi is None:
        hi = len(input) - 1
    # There is no binary search tree available (lo cannot be greater thatn hi when refering to bsts)
    if lo > hi:
        return None
    
    # Calculate the middle index of the input
    mid = (lo + hi) // 2
    # Assign a key & value to the node in the middle
    key, value = input[mid]

    # Create the root node
    root = BSTNode(key, value)
    # Assign the roots parent to be the provided parent(None if no parent is provided)
    root.parent = parent
    # Recursively create left & right subtrees by dividing the array/list per iteration
    root.left = make_balanced_bst(input, lo, mid-1, root)
    root.right = make_balanced_bst(input, mid+1, hi, root)

    # Return the root node which contains the entire outputted tree
    return root

def balanced_bst(node):
    """Wrapper function that lists the tree outputted from make_balanced_bst"""
    return make_balanced_bst(list_all(node))
