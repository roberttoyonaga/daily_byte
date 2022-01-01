#include <queue> // functional,iostream,ctime,cstdlib
#include <cmath>   //abs
#include <iostream>
using namespace std;

int ThrowingStones(vector<int> stones)
{
    priority_queue<int> stonesPQ(stones.begin(), stones.end()); // default is max . Use std::greater<int> to get a min prio queue 

    while(stonesPQ.size() > 1)
    {
        int stone1 = stonesPQ.top(); //use top() because pop() is a void function and returns nothing
        stonesPQ.pop();
        int stone2 = stonesPQ.top();
        stonesPQ.pop();  

        if (stone1 == stone2) continue;
        stonesPQ.push(abs(stone1-stone2));

    }

    if (stonesPQ.size()==0)
    {
        return 0;
    }
    return stonesPQ.top();
}

int main(int argc, char* argv[])
{
    cout<<ThrowingStones(vector<int>{1, 2, 3, 4});
    //cout<<ThrowingStones(vector<int>{2, 4, 3, 8});

}