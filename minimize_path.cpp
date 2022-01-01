#include <deque>
#include <vector>
#include <iostream>
using namespace std;
//assume top left is [0,0] and bottom right is [N-1, M-1]
//this is a DP problem
int minimizePath(vector<vector<int>>& arr)
{
    for (int row = 0; row < arr.size(); ++row)
    {
        for ( int col = 0; col < arr[0].size(); ++col)
        {
            //starting position
            if (row == 0 && col == 0) 
            {
                continue;
            }
            //top row
            else if (row ==0 )
            {
                arr[row][col] += arr[row][col-1];
            }
            // left most column
            else if (col == 0 )
            {
                arr[row][col] += arr[row-1][col];
            }
            // otherwise the min cost to reach this element is the min(element above, element to left) + target element
            else
            {
                arr[row][col] += min(arr[row-1][col], arr[row][col-1]);
            }

            
        }
    }
    return arr[arr.size()-1][arr[0].size()-1];
}

int main()
{
    vector<vector<int>> arr{{1,1,3},
                            {2,3,1},
                            {4,6,1}};
    
    cout<< minimizePath(arr);

    //this output array shows the min cost to reach each element
    for (const vector<int> row : arr)
    {
        cout<<"\n";
        for (const int col : row)
        {
            cout<<col<<" ";
        }
    }
}