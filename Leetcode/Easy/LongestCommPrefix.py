class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs) == 1:
            return strs[0]
        
        prefix = ""
        end = False

        # Iterate over letters 1st String
        for c in range(0, len(strs[0])):
            # Iterate over list of Strings
            for l in range(1, len(strs)):
                # If char index is still is not null and egal to firstString 
                if c < len(strs[l]) and strs[0][c] == strs[l][c]:
                    continue
                else:
                    end = True
                    break
            if end:
                break
            
            prefix = prefix + strs[0][c]          

        return prefix
