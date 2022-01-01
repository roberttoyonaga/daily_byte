#include <vector>
#include <iostream>
using namespace std;

int stairs(int nStairs)
{
    vector<int> dp;
    dp.reserve(nStairs);
    dp.push_back(1);//one way to get to step 0
    dp.push_back(2); //2 ways to get to step 2 (1+1 or 2)
    for (int i = 2; i < nStairs; i++)
    {
        dp.push_back(dp[i-1]+dp[i-2]);
    }
    return dp.back();
}

int stairs_2(int nStairs)
{
    int count = 0;
    for (int i = 0; i < nStairs-1; i++)
    {
        count ++;// 1step
        count ++;// 2 step  //WRONG because if you increase 2  steps you need to increase 1 twice
    }
    count++;
    return count;
}

int main()
{
    cout<<stairs(3)<<" "<<"3 ";
    cout<<stairs(4)<<" "<<"5 "; // 1+1+1+1,2+2,1+1+2,2+1+1,1+2+1
    cout<<stairs(5)<<" "<<"8 "; // 1+1+1+1+1, 2+1+1+1, 2+2+1, 1+2+1+1, 1+1+2+1, 1+1+1+2,  1+2+2, 2+1+2
    cout<<stairs(6)<<" "<<"? "<<endl;

    cout<<stairs_2(3)<<" "<<"3 ";
    cout<<stairs_2(4)<<" "<<"5 ";
    cout<<stairs_2(5)<<" "<<"8 ";
    cout<<stairs_2(6)<<" "<<"? ";
}