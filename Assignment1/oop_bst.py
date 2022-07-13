#Matthew Kenny 
#17470802
#Resources used for reasearch : 
#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
#Wikipedia : https://en.wikipedia.org/wiki/Binary_tree
#Youtube : Python: Binary Search Tree - BST (channel name: Joe James)
#Online pdf : http://cslibrary.stanford.edu/110/BinaryTrees.pdf
#Course notes : https://www.computing.dcu.ie/~davids/courses/CA341/CA341.html
class Phonebook:
    def __init__(self, name, address, phone_number):
        # this is the data part
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.left = None #Left pointer
        self.right = None #right pointer
        
    def insert(root, key):
        # here key is another Phonebook, not just a number
        if root is None:
            return key
        else:
            # now we compare the names
            # if we have the same name return the root
            if root.name == key.name:
                return root
            # if root.name is less the key.name then insert it into right
            # ex root.name = 'a' and key.name = 'b'
            elif root.name < key.name:
                root.right = insert(root.right, key)
            # else vice versa
            else:
                root.left = insert(root.left, key)
        # return the root
        return root    
      
def comparing_strings(string1, string2): #Function comparing two strings 
    if (string1 == string2):
        raise Exception("String one and String two are the same string")
    for s1, s2 in zip(string1, string2):
        # ord returns the ascii index of char
        if ord(s1) < ord(s2):
            return True
        if ord(s1) > ord(s2):
            return False
        # If the conditions arent True then binary Tree simply wont work
    return len(s1) > len(s2)

    # A utility function to do inorder tree traversal 
    def traversal(root): 
        if root: 
            traversal(root.left) 
            print(root.value) 
            traversal(root.right) 
    
class Node:
    def __init__(self, value, data=None):
        self.value = value
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"<Node value={repr(self.value)} left={repr(self.left)} right={self.right}>"

    def insert(self, node, compare_fn):
        if compare_fn(self.value, node.value) > 0:
            if self.right == None:
                self.right = node
            else:
                self.right.insert(node, compare_fn)
        else:
            if self.left == None:
                self.left = node
            else:
                self.left.insert(node, compare_fn)
                
    def search(self, value, compare_fn):
        if self.value == value:
            return self.data
        else:
            if compare_fn(self.value, value) > 0:
                if self.right == None:
                    return None
                else:
                    return self.right.search(value, compare_fn)
            else:
                if self.left == None:
                    return None
                else:
                    return self.left.search(value, compare_fn)

class ContactBinaryTree:
    def __init__(self, compare_fn):
        self.head = None
        self.compare_fn = compare_fn

    def __repr__(self):
        # im going to write this later
        return f"<BinaryTree head={self.head}>"

    def search(self, value):
        if self.head == None:
            return None
        return self.head.search(value, self.compare_fn)

    def insert(self, node):
        if self.head != None:
            self.head.insert(node, self.compare_fn)
        else:
            self.head = node

class PhoneBookEntry:
    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number
    def __repr__(self):
        return f"<PhoneBookEntry name={self.name} address={self.address} number={self.number}>"


phonebook_records = [
    PhoneBookEntry("Darragh", "Tyrone", "0851234567"),
    PhoneBookEntry("Sarah", "Mayo", "0861234567"),
    PhoneBookEntry("Diarmuid", "Dublin", "0871234567"),
    PhoneBookEntry("Amy", "Wicklow", "0591234567"),
    PhoneBookEntry("Oisin", "Kerry", "0831234567")
    ]



name_bst = ContactBinaryTree(comparing_strings)
phone_number_bst = ContactBinaryTree(comparing_strings)


for contact in phonebook_records:
    # print(contact)
    name_bst.insert(Node(contact.name, contact))
    phone_number_bst.insert(Node(contact.number, contact))







#Search by name

print(f"Get {name_bst.search('Oisin').name}'s' phone number -> {name_bst.search('Oisin').number}")
print(f"Get {name_bst.search('Darragh').name}'s' phone number -> {name_bst.search('Darragh').number}")
print(f"Get {name_bst.search('Diarmuid').name}'s' phone number -> {name_bst.search('Diarmuid').number}")
print(f"Get {name_bst.search('Amy').name}'s' phone number -> {name_bst.search('Amy').number}")
print(f"Get {name_bst.search('Sarah').name}'s' phone number -> {name_bst.search('Sarah').number}")




print('*' * 40)

#Search by phone number
print(f"Get {phone_number_bst.search('0831234567').name}'s' address -> {phone_number_bst.search('0831234567').address}")
print(f"Get {phone_number_bst.search('0851234567').name}'s' address -> {phone_number_bst.search('0851234567').address}")
print(f"Get {phone_number_bst.search('0871234567').name}'s' address -> {phone_number_bst.search('0871234567').address}")
print(f"Get {phone_number_bst.search('0591234567').name}'s' address -> {phone_number_bst.search('0591234567').address}")
print(f"Get {phone_number_bst.search('0861234567').name}'s' address -> {phone_number_bst.search('0861234567').address}")