#Matthew Kenny 
#17470802
#Resources used for reasearch : 
#https://www.geeksforgeeks.org/binary-search-tree-set-1-search-and-insertion/
#Wikipedia : https://en.wikipedia.org/wiki/Binary_tree
#Youtube : Python: Binary Search Tree - BST (channel name: Joe James)
#Online pdf : http://cslibrary.stanford.edu/110/BinaryTrees.pdf
#Course notes : https://www.computing.dcu.ie/~davids/courses/CA341/CA341.html
def dfs(node):
    "Print the node value in DFS order"
    left_child, data, right_child = node
    # print(data)
    if left_child is not None:
        dfs(left_child)
    if right_child is not None:
        dfs(right_child)

def insert(node, new_data, field_idx):
    left_child, data, right_child = node
    if data is None:
        return (None, new_data, None)
    
    if new_data[field_idx] <= data[field_idx]:
        if left_child is None:
            new_node = (None, new_data, None)
            return (new_node, data, right_child)
        left_child = insert(left_child, new_data, 0)
        return (left_child, data, right_child)

    if new_data[field_idx] > data[field_idx]:
        if right_child is None:
            new_node = (None, new_data, None)
            return (left_child, data, new_node)
        right_child = insert(right_child, new_data, 0)
        return (left_child, data, right_child)



def search_by(node, value, field):
    if not node:
        return None
    if node[VALUE][field] == value:
        return node[VALUE]
    if node[VALUE][field] < value:
        return search_by(node[RIGHT], value, field)
    return search_by(node[LEFT], value, field)


# All contacts (c = contact) 
c1 = ("Jason", "London", "004400")
c2 = ("Noel", "Wigan", "004401")
c3 = ("Peter", "Middlesbrough", "004402")
c4 = ("Danny", "Coventry", "004403")
c5 = ("Steven", "Liverpool", "004404")


LEFT, VALUE, RIGHT = 0,1,2 #Constant variables , VALUE = whole tuple
NAME,ADDRESS,NUMBER = 0,1,2 #Constant variables 



root = (None, None, None)

root = insert(root, c1, NAME)
root = insert(root, c2, NAME)
root = insert(root, c3, NAME)
root = insert(root, c4, NAME)
root = insert(root, c5, NAME)

# root2 = (None, None, None)

# root2 = insert(root2, c1, ADDRESS)
# root2 = insert(root2, c2, ADDRESS)
# root2 = insert(root2, c3, ADDRESS)
# root2 = insert(root2, c4, ADDRESS)
# root2 = insert(root2, c5, ADDRESS)

root3 = (None,None,None)
root3 = insert(root3, c1, NUMBER)
root3 = insert(root3, c2, NUMBER)
root3 = insert(root3, c3, NUMBER)
root3 = insert(root3, c4, NUMBER)
root3 = insert(root3, c5, NUMBER)
# print(name_bst)
# print(root)
# print(root2)
# print(root3)
# print(address_bst)
# print("*" * 40)

print(f"Get {search_by(root,'Noel',field=NAME)[NAME]}'s phone number ->  {search_by(root,'Noel',field=NAME)[NUMBER]}")
print(f"Get {search_by(root,'Jason',field=NAME)[NAME]}'s phone number ->  {search_by(root,'Jason',field=NAME)[NUMBER]}")
print(f"Get {search_by(root,'Steven',field=NAME)[NAME]}'s phone number ->  {search_by(root,'Steven',field=NAME)[NUMBER]}")
print(f"Get {search_by(root,'Peter',field=NAME)[NAME]}'s phone number ->  {search_by(root,'Peter',field=NAME)[NUMBER]}")
print(f"Get {search_by(root,'Danny',field=NAME)[NAME]}'s phone number ->  {search_by(root,'Danny',field=NAME)[NUMBER]}")
# print(search_by(root2,"Wigan",field=ADDRESS))
print("*" * 40)
print(f"Get {search_by(root3,'004400',field=NUMBER)[NAME]}'s address ->  {search_by(root3,'004400',field=NUMBER)[ADDRESS]}")
print(f"Get {search_by(root3,'004401',field=NUMBER)[NAME]}'s address ->  {search_by(root3,'004401',field=NUMBER)[ADDRESS]}")
print(f"Get {search_by(root3,'004402',field=NUMBER)[NAME]}'s address ->  {search_by(root3,'004402',field=NUMBER)[ADDRESS]}")
print(f"Get {search_by(root3,'004404',field=NUMBER)[NAME]}'s address ->  {search_by(root3,'004404',field=NUMBER)[ADDRESS]}")