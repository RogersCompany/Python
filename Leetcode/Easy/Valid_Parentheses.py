class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            if st:
                last = st[-1]
                if self.test_ord(last, s[i]):
                    st.pop()
                    continue
            st.append(s[i])
        
        return not st
    
    def test_ord(self, last, cur):
        if ord(last)+1 == ord(cur) or ord(last)+2 == ord(cur):
            return True
        return False