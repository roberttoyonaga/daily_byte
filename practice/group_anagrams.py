class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_sets = {}
        for s in strs:
            sorted_str = "".join(sorted(s))
            if sorted_str in anagram_sets:
                anagram_sets[sorted_str].append(s)
            else:
                anagram_sets[sorted_str] = [s]
        ret = []
        for key in anagram_sets:
            ret.append(anagram_sets[key])
        return ret
        
        