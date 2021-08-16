#include <iostream>

class Node
{
private:

public:
    Node(int newData);
    int data;
    Node* leftChild;
    Node* rightChild;
};

Node::Node(int newData)
{
    data = newData;
    leftChild = nullptr;
    rightChild = nullptr;
}

void binaryInsert(Node* root, Node* node)
{
    if (!root)
    {
        return;
    }
    else
    {
        if (root->data > node->data)
        {
            if (!root->leftChild)
            {
                root->leftChild = node;
            }
            else
            {
                binaryInsert(root->leftChild, node);
            }
        }
        else
        {
            if (!root->rightChild)
            {
                root->rightChild = node;
            }
            else
            {
                binaryInsert(root->rightChild, node);
            }
        }
    }
}

void inOrderPrint(Node* root)
{
    if (!root)
    {
        return;
    }
    inOrderPrint(root->leftChild);
    std::cout<< root->data <<std::endl;
    inOrderPrint(root->rightChild);
}