#include <iostream>
#include <vector>
using namespace std;
int util(vector<int>& arr, int start, int end, vector<vector<int>> &m)
{
    //stopping condition
    if (start==end)
    {
        return arr[start];
    }
    // cached cased
    if (m[start][end]!=0)
    {
        return m[start][end];
    }
    int opt1 = arr[start] - util(arr, start+1, end, m);
    int opt2 = arr[end] - util(arr, start, end - 1, m);
    m[start][end] = std::max(opt1,opt2);
    return m[start][end];
}
int WhoWins(vector<int>& arr)
{
    // Initializing a single row
    vector<int> row(arr.size(), 0);
 
    // Initializing the 2-D vector
    vector<vector<int>> m(arr.size(), row);

    if (util(arr, 0, arr.size()-1, m)>0) return 1;
    return 2;
}




int main(int argc, char* argv[])
{
    vector<int> arr=  {1, 2, 3};
    cout<<WhoWins(arr);

}