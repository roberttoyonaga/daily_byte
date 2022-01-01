#include <iostream>
#include <algorithm>    // std::max
#include "bst.h"

// int main()
// {
//     Node n1 = Node(4);
//     Node n2 = Node(5);
//     Node n3 = Node(14);

//     Node n4 = Node(1);


//     Node bst = Node(3);
//     binaryInsert(&bst, &n1);
//     binaryInsert(&bst, &n2);
//     binaryInsert(&bst, &n3);
//     binaryInsert(&bst, &n4);
//     inOrderPrint(&bst);

// }

int bstMaxDepth(Node* root, int depth)
{
    if (!root)
    {
        return depth;
    }
    return  std::max( bstMaxDepth( root->leftChild, depth + 1), bstMaxDepth( root->rightChild, depth + 1) );

}

int main()
{
    Node n1 = Node(4);
    Node n2 = Node(5);
    Node n3 = Node(14);
    Node n4 = Node(1);
    Node n5 = Node(2);
    Node n6 = Node(15);


    Node bst = Node(3);

    binaryInsert(&bst, &n1);
    binaryInsert(&bst, &n2);
    binaryInsert(&bst, &n3);
    binaryInsert(&bst, &n4);
    binaryInsert(&bst, &n5);    
    binaryInsert(&bst, &n6);

    std::cout<< bstMaxDepth(&bst,0);
}