#include <iostream>
#include "bst.h"

bool Util(Node* root, int max, int min)
{
    if (!root) //stopping condition
    {
        return true;
    }
    else if ( (min!= NULL && root->data < min) || (max!= NULL && root->data > max) )
    {
        return false;
    }
    else
    {
        return Util(root->leftChild, root->data, min) && Util(root->rightChild, max,root->data);
    }
}

bool ValidateBST(Node* bst)
{
    return Util(bst, NULL, NULL);
}



int main()
{
    Node n1 = Node(4);
    Node n2 = Node(5);
    Node n3 = Node(14);
    Node n4 = Node(1);
    Node n5 = Node(2);
    Node n6 = Node(15);
    Node n7 = Node(100000);
    n6.leftChild = &n7; //should cause make it invalid

    Node bst = Node(3);

    binaryInsert(&bst, &n1);
    binaryInsert(&bst, &n2);
    binaryInsert(&bst, &n3);
    binaryInsert(&bst, &n4);
    binaryInsert(&bst, &n5);    
    binaryInsert(&bst, &n6);

    std::cout<< ValidateBST(&bst);
}