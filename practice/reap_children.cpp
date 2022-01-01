#include <vector>
#include <unordered_map>
#include <iostream>
#include <queue>

using namespace std;

vector<int> ReapChildren(vector<int> &pid, vector<int> &parentPid, int kill)
{
    //get a map
    unordered_map<int,vector<int>> parentToChildren;
    int child = 0;
    for (int parent : parentPid)
    {
        if (parentToChildren.find(parent) == parentToChildren.end())
        {
            parentToChildren[parent] = vector<int> ({pid[child]});
        }
        else
        {
             parentToChildren[parent].push_back(pid[child]);
        }
        child++;
    }

    vector<int> processesToKill;
    queue<int> q;
    q.push(kill);
    while(!q.empty())
    {
        int current = q.front();
        q.pop();
        processesToKill.push_back(current);
        if (parentToChildren.find(current)==parentToChildren.end()) continue;
        for (int child : parentToChildren[current])
        {
            q.push(child);
        }

    }
    return processesToKill;
}

int main()
{
    vector<int> pid{2, 4, 3, 7}; 
    vector<int> ppid{0, 2, 2, 3}; 
    vector<int> out = ReapChildren(pid, ppid, 3);
    for (int kill : out)
    {
        cout<<kill<<endl;
    }
}