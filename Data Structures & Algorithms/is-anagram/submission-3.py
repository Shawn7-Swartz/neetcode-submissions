class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        t1 = sorted(t)
        if len(s)!=len(t):
            return False
        
        seen={}
        for i in s1:
            seen[i] = s.count(i)

        for i in t1:
            if i in seen:
                seen[i] -=1 # to keep balance of both strings while checking for same elements
            else:
                return False #it checks whether both the strings have same characters or not

        for count in seen.values():
            if count !=0:
                return False # checking whether all the elements have been checked or not
        return True

        