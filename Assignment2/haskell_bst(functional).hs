-- Student name : Matthew Kenny
-- Student number : 17470802
-- Resources used for reasearch : 
-- https://www101.dcu.ie/registry/module_contents.php?function=2&subcode=CA320 (Done Haskell binary search trees in module before )
-- Please Note CA320 module notes require login details , please see link below for open source notes
-- https://www.computing.dcu.ie/~davids/courses/CA320/CA320.html
-- https://hackage.haskell.org/package/type-indexed-queues-0.2.0.0/docs/Data-BinaryTree.html
-- http://hackage.haskell.org/package/tree-traversals-0.1.1.0/docs/Data-Traversable-TreeLike.html


--Create data structure 
data BinaryTree tree = Empty | Node (BinaryTree tree) tree (BinaryTree tree) 
    deriving (Show)

--Using node constrcutor
insertNodes :: (Ord tree) => tree -> BinaryTree tree -> BinaryTree tree  
insertNodes inputValue Empty = Node (Empty) inputValue (Empty)  
insertNodes inputValue (Node  left value right)   
    | inputValue == value = Node left inputValue right  
    | inputValue < value  = Node (insertNodes inputValue left) value right  
    | inputValue > value  = Node  left value (insertNodes inputValue right) 


--Search , tree = is generic 
searchNodes :: (Ord tree) => BinaryTree tree -> tree -> Bool 
searchNodes Empty query = False 
searchNodes (Node leftNode value rightNode) query 
  | value == query = True 
  | query < value = searchNodes leftNode query
  | query > value = searchNodes rightNode query
  

--breadth first search 
preOrderTraversal :: BinaryTree tree -> [tree] 
preOrderTraversal Empty = []
preOrderTraversal (Node leftNode value rightNode) = [value] ++ preOrderTraversal leftNode ++ preOrderTraversal rightNode

--Notice change of increment
inOrderTraversal :: BinaryTree tree -> [tree] 
inOrderTraversal Empty = []
inOrderTraversal (Node leftNode value rightNode) = inOrderTraversal leftNode ++ [value] ++ inOrderTraversal rightNode

--Notice change of increment
postOrderTraversal :: BinaryTree tree -> [tree] 
postOrderTraversal Empty = []
postOrderTraversal (Node leftNode value rightNode) = postOrderTraversal leftNode ++ postOrderTraversal rightNode ++ [value]


--Run program to see test cases 
main :: IO()
main = do
    let bt = foldr insertNodes (Empty) [4,3,1,2]
    print (bt)
    print (preOrderTraversal bt)
    print (inOrderTraversal bt)
    print (postOrderTraversal bt)
    print (searchNodes bt 1)
    print (searchNodes bt 5)