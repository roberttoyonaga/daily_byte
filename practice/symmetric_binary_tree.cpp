#include <iostream>
#include <vector>
#include "bst.h"


bool util(Node* left, Node* right)
{
    if (!left && ! right)
    {
        return true;
    }

    if (left && right && left->data == right->data)
    {
        return util(left->leftChild, right->rightChild) && util(left->rightChild, right->leftChild);
    }

    return false;
}

bool isSymmetric(Node* root)
{
    return util(root->leftChild, root->rightChild);
} 

int main()
{
    Node bst = Node(4);
    Node n1 = Node (3);
    Node n2 = Node (3);

    bst.leftChild = &n1;
    bst.rightChild = &n2;

    Node n3 = Node(2);
    Node n4 = Node(2);

    n1.leftChild = &n3;
    n2.rightChild = &n4;

    std::cout<<isSymmetric(&bst);
}