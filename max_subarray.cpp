#include <deque>
#include <vector>
#include <iostream>
using namespace std;

/*
The key:
    - At each element we visit we have two choices
        - continue our sequence (that yeilds the max)
        - start a new sequence
    - by the time we've visited all elements, each sequence will have been maximized so that its sum will the biggest it can possibly be
    - Now simply see which sequence is biggest (or keep a variable "max")
*/
int max_subarray(vector<int>& arr)
{
    int curr =0;
    int max = 0;
    for(const auto& num : arr)
    {
        // start new sequence
        if (num > curr + num)
        {
            curr = num;
        }
        //continue old sequence
        else 
        {
            curr += num;
        }

        //update max
        if (max < curr)
        {
            max = curr;
        }

    }
    return max;
}
int main()
{
    //std::vector<int> arr{-3,8,-8,2};
    std::vector<int> arr{1, 5,-2, -3, 7};
    
    cout<< max_subarray(arr);
}
