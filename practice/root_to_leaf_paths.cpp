#include <iostream>
#include <vector>
#include "bst.h"

void rootToLeafPaths(Node* root, std::vector<int> &currentPath, std::vector<std::vector<int>> &finalResult)
{
    // if null then append current path and stop (must mean that other child of parent is non null)
    if (!root)
    {
        finalResult.push_back(currentPath);
        return;
    }

    currentPath.push_back(root->data);

    //copy current path
    std::vector<int> currentPath2 = std::vector<int>(currentPath);

    // at least one child is non null. Continue recursion
    if (root->leftChild || root->rightChild)
    {
        rootToLeafPaths( root->leftChild, currentPath, finalResult);
        rootToLeafPaths( root->rightChild, currentPath2, finalResult);
    }
    //if both children are null, append and stop recursion. Avoid adding same path twice (if we recur)
    else if (!root->leftChild && !root->rightChild)
    {
        finalResult.push_back(currentPath);
        return;
    }

}

int main()
{
    Node n1 = Node(4);
    Node n2 = Node(5);
    Node n3 = Node(8);
    Node n4 = Node(1);
    Node n5 = Node(2);
    Node n6 = Node(9);


    Node bst = Node(3);

    binaryInsert(&bst, &n1);
    binaryInsert(&bst, &n2);
    binaryInsert(&bst, &n3);
    binaryInsert(&bst, &n4);
    binaryInsert(&bst, &n5);    
    binaryInsert(&bst, &n6);

    std::vector<std::vector<int>> result;
    std::vector<int> start;
    rootToLeafPaths(&bst, start, result);

    // print result
    for (int i = 0; i < result.size(); i++)
    {
        for (int j = 0; j < result[i].size(); j++)
        {
            std::cout << result[i][j];
        }
         std::cout <<std::endl;
    }
}