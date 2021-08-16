class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> result;
        util(n, 0,0,"",result);
        return result;
    }
    
    void util(int n, int left, int right, string current, vector<string> &result)
    {
        if ( right == n )
        {
         result.push_back(current);
         return;
        }
        if (left<n)
        {
            util(n, left+1, right, current + "(", result);
        }
        if (right < left)
        {
            util(n, left, right+1, current+ ")", result);
        }
    
        
    }
};