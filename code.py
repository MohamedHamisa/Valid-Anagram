class Solution:
    def isAnagram(self, s: str, t: str):
        return Counter(s) == Counter(t)

      '''
      or

def isAnagram(self, s: str, t: str):
    return all(s.count(x) == t.count(x) for x in string.ascii_lowercase)
    
    '''
