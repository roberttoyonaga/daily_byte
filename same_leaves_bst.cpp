#include <iostream>
#include <vector>
#include "bst.h"

// do two inorder traversals

void inOrder(Node* root, std::vector<int>& vec)
{
    if(!root)
    {
        return;
    }

    inOrder(root->leftChild, vec);
    if(!root->leftChild && !root->rightChild)
    {
        vec.push_back(root->data);
    }
    inOrder(root->rightChild, vec);
}
bool sameLeaves(Node* root1, Node* root2)
{
    std::vector<int> leaves1;
    std::vector<int> leaves2;
    inOrder(root1, leaves1);
    inOrder(root2, leaves2);
    if (leaves1.size() != leaves2.size()) return false;
    
    for (int i=0 ; i< leaves1.size(); i++)
    {
        if (leaves1[i]!=leaves2[i]) return false;
    }
    return true;
}


int main()
{
    Node bst1 = Node(4);
    Node n1 = Node (3);
    Node n2 = Node (3);

    bst1.leftChild = &n1;
    bst1.rightChild = &n2;

    Node n3 = Node(2);
    Node n4 = Node(6);

    n1.leftChild = &n3;
    n2.rightChild = &n4;

    Node bst2 = Node(4);
    Node n5 = Node (1);
    Node n6 = Node (33);

    bst2.leftChild = &n5;
    bst2.rightChild = &n6;

    Node n7 = Node(2);
    Node n8 = Node(6);

    n5.leftChild = &n7;
    n6.rightChild = &n8;

    std::cout<<sameLeaves(&bst1, &bst2);
}