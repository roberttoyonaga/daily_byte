//sliding window approach

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<char, int> window;
        int left = 0;
        int right = 0;
        int result = 0;
        
        while (right != s.length())
        {
            
            char r = s[right];
            if (window.find(r)==window.end())
            {
                window[r] = 1;
            }
            else
            {
                window[r] += 1;
            }
            
            while (window[r] > 1)
            {
                window[s[left]] -= 1;
                left++;
            }
            result = max(result, right - left + 1);
            right++;
            
        }
        return result;
        
    }
};