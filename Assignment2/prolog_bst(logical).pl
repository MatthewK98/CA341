/* Student name : Matthew Kenny
 Student number : 17470802
 Resources used for reasearch : 
 https://www.swi-prolog.org/pldoc/index.html : I used the swi-prolog docs as a manual to help myself compiling the program and any errors/bugs I ran into.
 https://www.computing.dcu.ie/~davids/CA208_Prolog_2p.pdf : I read over CA208 notes to go over prolog fundamentals again and thought me how to create binary trees in the prolog language
 https://www3.cs.stonybrook.edu/~pfodor/courses/CSE595/L09_Prolog.pdf : Used for traversal algorithms , although preorder algorithm works succesfully , postorder and inorder gives mixed outputs. 
 */




/* Search predicate */
searchTree(Value, binaryTree(_, Value, _)).

/* Check Right Side*/
searchTree(Value, binaryTree(_, SecondValue, RightNode)) 
    :- SecondValue =< Value,
     searchTree(Value,RightNode)
     .

/* Check Left Side*/
searchTree(Value, binaryTree(LeftNode, SecondValue, _)) 
    :-SecondValue >= Value,
    searchTree(Value, LeftNode)
    .


/* Insert predicate */

insertNodes(_, Value, binaryTree(_, Value, _)).

/* Check Right Side*/
insertNodes(binaryTree(LeftNode,SecondValue,RightNode),
    Value,binaryTree(LeftNode,SecondValue,RightNode1)) 
    :- insertNodes(RightNode,Value,RightNode1)
    .

/* Check Left Side*/
insertNodes(binaryTree(LeftNode,SecondValue,RightNode), 
    Value, binaryTree(LeftNode1,SecondValue,RightNode)) 
    :- Value=<SecondValue,
    insertNodes(LeftNode,Value,LeftNode1)
    .







/* preorder predicate */
preorder_Traversal(binaryTree(Value, void, void), 
    [Value]) :- !.

/* Check Left Side*/
preorder_Traversal(binaryTree(Value, LeftNode, _RightNode), 
    [Value|ValueTails]) :- preorder_Traversal(LeftNode, ValueTails).

/* Check Right Side*/
preorder_Traversal(binaryTree(Value, _LeftNode, RightNode), 
    [Value|ValueTails]) :- preorder_Traversal(RightNode, ValueTails).



/* postorder predicate */
postorder_Traversal(binaryTree(Value, _, _).

/* Check Left Side*/
postorder_Traversal(binaryTree(Value, LeftNode, _RightNode), [Value|ValueTails]) :- postorder_Traversal(_, ValueTails).

/* Check Right Side*/
postorder_Traversal(binaryTree(Value, _LeftNode, RightNode), [Value|ValueTails]) :- postorder_Traversal(_, ValueTails).


/* inorder predicate */
inorder_Traversal(binaryTree(Value, _, _) :- [Value|ValueTails]) :- inorder_Traversal(ValueTails).



/* Tester code  */ 


/* Test preorder */ 
X = tree(a, tree(b, void, void), void), prolog_tutorial(X, Res).


test_tree(
    binaryTree(
        binaryTree(binaryTree(nil, 3, nil), 5, binaryTree(nil, 6, nil)),
        20,
        nil
    )
).





/* Expected true  */ 
test_search :-
    test_tree(X),searchTree(20, X).

/* Expected true  */ 
test2_search :- 
    test_tree(X), searchTree(5, X).

/* Expected true  */ 
test3_search :-
    test_tree(X),searchTree(3, X).

/* Expected false  */ 
test4_search :- 
    test_tree(X), searchTree(7, X).